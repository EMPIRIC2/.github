"""Headline figure for the EMPIRIC organization README.

Two panels at the same map extent over Viti Levu, Fiji:
  left   2-m air temperature on a 0.25 degree grid (about 30 km), the
         resolution of global reanalysis products
  right  the same field on a 2.5 km grid, the island-scale target of the
         EMPIRIC downscaling work

The fields are SYNTHETIC. They are built from a real coastline (Natural
Earth 1:10m, public domain) and a made-up smooth elevation surface with a
fixed lapse rate, so the figure illustrates the resolution gap and nothing
else. To show real output, replace `synthetic_fields()` with a function
that returns (lon2d, lat2d, fine_temperature) and leave the rest alone.

Run:  python make_downscaling_figure.py
Writes downscaling_schematic_light.png and downscaling_schematic_dark.png
next to this script.
"""
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from scipy import ndimage

HERE = Path(__file__).resolve().parent

# Map window (degrees). Viti Levu spans roughly 177.25-178.71 E, 18.27-17.30 S.
LON0, LON1 = 176.95, 179.00
LAT0, LAT1 = -18.55, -17.05
FINE_DEG = 0.0225           # 2.5 km at 18 S
COARSE_DEG = 0.25           # ~27 km, the ERA5 grid spacing
LAPSE_K_PER_M = 0.0065      # standard tropospheric lapse rate


def coastline():
    rings = json.loads((HERE / "vitilevu_coast.json").read_text())
    return [np.asarray(r) for r in rings]


def synthetic_fields(rings):
    """Return lon2d, lat2d, fine temperature (deg C). Synthetic, see header."""
    lon = np.arange(LON0, LON1, FINE_DEG)
    lat = np.arange(LAT0, LAT1, FINE_DEG)
    lon2d, lat2d = np.meshgrid(lon, lat)

    # Land mask from the coastline polygon.
    pts = np.column_stack([lon2d.ravel(), lat2d.ravel()])
    land = np.zeros(lon2d.size, bool)
    for r in rings:
        land |= MplPath(r).contains_points(pts)
    land = land.reshape(lon2d.shape)

    # Elevation: a smooth surface that rises inland, highest along a ridge
    # running north-east through the centre-north of the island, as the real
    # highlands do (Mt Tomanivi, 1324 m, sits near 17.6 S, 178.0 E). The west
    # coast stays low. Made up, but with the right shape and magnitudes.
    dist_km = ndimage.distance_transform_edt(land) * 2.5
    km_lon = 111.32 * np.cos(np.deg2rad(17.8)); km_lat = 111.32
    x = (lon2d - 178.0) * km_lon; y = (lat2d + 17.65) * km_lat       # km from the ridge centre
    along = (x * 0.6 + y * 0.8); across = (-x * 0.8 + y * 0.6)         # rotate axes onto the ridge
    ridge = np.exp(-(across / 22.0) ** 2) * np.exp(-(along / 60.0) ** 2)
    taper = np.clip(dist_km / 14.0, 0, 1) ** 0.7                      # coastal plains stay low
    rng = np.random.default_rng(7)
    bumps = ndimage.gaussian_filter(rng.standard_normal(land.shape), 3.0)
    bumps = bumps / bumps.std()
    elev = taper * (1150.0 * ridge + 350.0) + 160.0 * taper * bumps
    elev = ndimage.gaussian_filter(elev, 1.0)
    elev = np.where(land, np.clip(elev, 0, 1350.0), 0.0)   # cap near the real summit height

    # Temperature: warm sea with a weak north-south gradient, land a little
    # warmer at the coast, cooling with height.
    sea_t = 27.3 + 0.6 * (lat2d - LAT0) / (LAT1 - LAT0)
    land_t = 28.4 - LAPSE_K_PER_M * elev
    temp = np.where(land, land_t, sea_t)
    temp = ndimage.gaussian_filter(temp, 0.6)   # soften the coastal step
    return lon2d, lat2d, temp


def block_average(lon2d, lat2d, field):
    """Average the fine field onto a COARSE_DEG grid aligned to multiples of COARSE_DEG."""
    lon_edges = np.arange(np.floor(LON0 / COARSE_DEG) * COARSE_DEG, LON1 + COARSE_DEG, COARSE_DEG)
    lat_edges = np.arange(np.floor(LAT0 / COARSE_DEG) * COARSE_DEG, LAT1 + COARSE_DEG, COARSE_DEG)
    i = np.digitize(lon2d.ravel(), lon_edges) - 1
    j = np.digitize(lat2d.ravel(), lat_edges) - 1
    coarse = np.full((len(lat_edges) - 1, len(lon_edges) - 1), np.nan)
    for jj in range(coarse.shape[0]):
        for ii in range(coarse.shape[1]):
            m = (i == ii) & (j == jj)
            if m.any():
                coarse[jj, ii] = field.ravel()[m].mean()
    return lon_edges, lat_edges, coarse


def draw(theme, lon2d, lat2d, temp, coarse_grid, rings, out):
    fg = "#1f2328" if theme == "light" else "#e6edf3"
    muted = "#59636e" if theme == "light" else "#9198a1"
    coast = "#111111" if theme == "light" else "#f0f6fc"
    edge = "#ffffff" if theme == "light" else "#0d1117"

    plt.rcParams.update({
        "font.family": ["DejaVu Sans", "sans-serif"],
        "text.color": fg, "axes.edgecolor": fg,
    })
    fig = plt.figure(figsize=(10, 4.6), dpi=200)
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.045], hspace=0.18, wspace=0.06,
                          left=0.02, right=0.98, top=0.88, bottom=0.14)
    axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])]
    cax = fig.add_subplot(gs[1, :])

    vmin, vmax = 19.0, 29.0
    cmap = "inferno"

    lon_edges, lat_edges, coarse = coarse_grid
    m0 = axes[0].pcolormesh(lon_edges, lat_edges, coarse, cmap=cmap, vmin=vmin, vmax=vmax,
                            shading="flat", edgecolors=edge, linewidth=0.5)
    axes[1].pcolormesh(lon2d, lat2d, temp, cmap=cmap, vmin=vmin, vmax=vmax,
                       shading="nearest", rasterized=True)

    titles = ["Reanalysis grid  ·  0.25°  (≈ 30 km)", "Downscaled  ·  2.5 km"]
    for ax, title in zip(axes, titles):
        for r in rings:
            ax.plot(r[:, 0], r[:, 1], color=coast, lw=0.8, solid_joinstyle="round")
        ax.set_xlim(LON0, LON1); ax.set_ylim(LAT0, LAT1)
        ax.set_aspect(1 / np.cos(np.deg2rad(17.8)))
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(title, loc="left", fontsize=10.5, color=fg, pad=8)

    # 50 km scale bar on the right panel.
    km_per_deg_lon = 111.32 * np.cos(np.deg2rad(17.8))
    x0, y0 = LON1 - 0.08 - 50 / km_per_deg_lon, LAT0 + 0.10
    axes[1].plot([x0, x0 + 50 / km_per_deg_lon], [y0, y0], color=coast, lw=1.6, solid_capstyle="butt")
    axes[1].text(x0 + 25 / km_per_deg_lon, y0 + 0.035, "50 km", ha="center", va="bottom",
                 fontsize=8.5, color=coast)
    axes[0].text(LON0 + 0.05, LAT0 + 0.08, "Viti Levu, Fiji", fontsize=8.5, color=coast, ha="left")

    cb = fig.colorbar(m0, cax=cax, orientation="horizontal")
    cb.set_label("2-m air temperature (°C)", fontsize=9.5, color=fg, labelpad=4)
    cb.ax.tick_params(labelsize=8.5, colors=fg, length=2.5)
    cb.outline.set_visible(False)

    fig.text(0.98, 0.015, "Schematic. Synthetic fields built on a real coastline; not model output.",
             ha="right", va="bottom", fontsize=7.5, color=muted)

    fig.savefig(out, transparent=True)
    plt.close(fig)


def main():
    rings = coastline()
    lon2d, lat2d, temp = synthetic_fields(rings)
    coarse_grid = block_average(lon2d, lat2d, temp)
    for theme in ("light", "dark"):
        draw(theme, lon2d, lat2d, temp, coarse_grid, rings, HERE / f"downscaling_schematic_{theme}.png")
        print("wrote", HERE / f"downscaling_schematic_{theme}.png")


if __name__ == "__main__":
    main()

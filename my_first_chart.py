import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Apple SD Gothic Neo"

prices = [72000, 69500, 72800, 72400, 70900]

fig, ax = plt.subplots(figsize = (7, 4))

fig.patch.set_facecolor("#0D1117")
ax.set_facecolor("#161B22")

ax.plot(
    prices,
    color = "#F0F6FC",
    linewidth = 2,
    marker = "o",
    markersize = 7,
    markerfacecolor = "#F0F6FC",
    markeredgecolor = "#161B22",
)

for i, p in enumerate(prices):
    ax.annotate(
        f"{p:,}",
        (i, p),
        textcoords = "offset points",
        xytext = (0, 10),
        ha = "center",
        color = "#F0F6FC",
        fontsize = 10,
    )

ax.grid(True, 
        color = "#30363D", 
        linewidth = 0.7,
        linestyle = "--",
        alpha = 0.8)
ax.tick_params(colors = "#8B949E", labelsize=9)

for spine in ax.spines.values():
    spine.set_color("#30363D")

ax.set_ylim(min(prices) - 500, max(prices) + 500)
ax.margins(x = 0.08)
ax.set_axisbelow(True)


ax.set_title(
    "내 첫 그래프",
    color = "#F0F6FC",
    fontsize = 16,
    pad = 15,
)
plt.tight_layout()
fig.savefig("my_first_chart.png", facecolor=fig.get_facecolor(), dpi = 200)

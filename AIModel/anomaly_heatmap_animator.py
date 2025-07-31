import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the AI anomaly log file
df = pd.read_csv("ai_anomaly_log.csv")

# Extract unique systems and time steps
systems = df["system"].unique()
time_steps = sorted(df["time"].unique())

# Set up the figure and one subplot per system
fig, axs = plt.subplots(len(systems), 1, figsize=(8, 1.5 * len(systems)), sharex=True)
if len(systems) == 1:
    axs = [axs]  # ensure it's iterable

# Initialize bars
bars = {}

for ax, system in zip(axs, systems):
    ax.set_title(system, loc="left", fontsize=10)
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 1)
    bar = ax.bar([0], [0.1], color="green")
    bars[system] = bar
    ax.set_yticks([])
    ax.set_xticks([])

# Update function for animation
def update(t):
    current_df = df[df["time"] == t]
    for system in systems:
        system_df = current_df[current_df["system"] == system]
        if not system_df.empty and system_df.iloc[0]["detected"] == "anomaly":
            bars[system][0].set_color("red")
            bars[system][0].set_height(1)
        else:
            bars[system][0].set_color("green")
            bars[system][0].set_height(0.1)
    fig.suptitle(f"AI Anomaly Detection Timeline — Time Step {t}", fontsize=12)

# Create animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=300, repeat=False)

# Save animation as GIF
ani.save("ai_anomaly_heatmap.gif", writer="pillow")
print("✅ Animation saved as ai_anomaly_heatmap.gif")

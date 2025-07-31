
import random
import matplotlib.pyplot as plt
import pandas as pd

# Simulation parameters
duration = 100  # time steps
systems = {
    "Cold Chain": {"normal_range": (2, 5), "anomaly_range": (8, 12)},
    "RFID Tags": {"normal_range": (0, 5), "anomaly_range": (10, 20)},
    "Cloud ERP": {"normal_range": (100, 200), "anomaly_range": (400, 600)},
    "Processing Robotics": {"normal_range": (0, 1), "anomaly_range": (5, 10)},
}

detection_accuracy = 0.85
false_positive_rate = 0.03

# Data store
records = []

for t in range(duration):
    for system, ranges in systems.items():
        if random.random() < 0.12:  # 2% chance of anomaly
            value = random.uniform(*ranges["anomaly_range"])
            actual = "anomaly"
            detected = "anomaly" if random.random() < detection_accuracy else "normal"
        else:
            value = random.uniform(*ranges["normal_range"])
            actual = "normal"
            detected = "anomaly" if random.random() < false_positive_rate else "normal"

        records.append({
            "time": t,
            "system": system,
            "value": value,
            "actual": actual,
            "detected": detected
        })

# Create DataFrame
df = pd.DataFrame(records)

# Save to CSV
df.to_csv("ai_anomaly_log.csv", index=False)

# Visualization
fig, axs = plt.subplots(len(systems), 1, figsize=(12, 8), sharex=True)

for i, system in enumerate(systems):
    sys_df = df[df["system"] == system]
    axs[i].plot(sys_df["time"], sys_df["value"], label=f"{system} value")
    axs[i].scatter(sys_df[sys_df["detected"]=="anomaly"]["time"], 
                   sys_df[sys_df["detected"]=="anomaly"]["value"],
                   color='red', marker='x', label="Detected Anomaly")
    axs[i].set_title(system)
    axs[i].legend(loc="upper right")

plt.xlabel("Time")
plt.tight_layout()
plt.savefig("ai_anomaly_plot.png")
plt.show()

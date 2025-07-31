
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
import os

# Load the most recent failure log CSV
files = [f for f in os.listdir('.') if f.startswith("failure_logs_") and f.endswith(".csv")]
if not files:
    print("No failure logs found.")
    sys.exit(1)

latest_file = sorted(files)[-1]
print(f"Loading: {latest_file}")
df = pd.read_csv(latest_file)

# Convert log into Gantt-style intervals
df['event'] = df['event'].str.strip()
failures = {}
for _, row in df.iterrows():
    system = row['system']
    time = row['time']
    if row['event'] == 'FAILED':
        failures.setdefault(system, []).append({'start': time, 'end': None})
    elif row['event'] == 'RECOVERED':
        if system in failures and failures[system][-1]['end'] is None:
            failures[system][-1]['end'] = time

# Build plot data
fig, ax = plt.subplots(figsize=(12, 8))
y_labels = list(failures.keys())
y_pos = range(len(y_labels))

for i, system in enumerate(y_labels):
    for interval in failures[system]:
        start = interval['start']
        end = interval['end'] if interval['end'] is not None else start + 1
        ax.barh(i, end - start, left=start, height=0.6, color='red')

ax.set_yticks(list(y_pos))
ax.set_yticklabels(y_labels)
ax.set_xlabel("Time")
ax.set_title("System Failure Timeline (Gantt View)")
red_patch = mpatches.Patch(color='red', label='Failure Period')
ax.legend(handles=[red_patch])

plt.tight_layout()
plt.savefig("failure_timeline.png")
plt.show()

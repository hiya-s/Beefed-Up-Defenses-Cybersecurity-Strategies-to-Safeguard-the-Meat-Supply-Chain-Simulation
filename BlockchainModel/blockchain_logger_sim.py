import pandas as pd
from datetime import datetime
import time
import random

# Simulate blockchain logging (replace with real Web3 later)
def simulate_blockchain_log(system, event_type):
    timestamp = int(time.time())
    print(f"[Blockchain] LOGGED: {system} | {event_type} | {timestamp}")
    return {
        "system": system,
        "event_type": event_type,
        "timestamp": timestamp
    }

def run_blockchain_simulation(log_file="failure_logs_latest.csv"):
    df = pd.read_csv(log_file)
    blockchain_logs = []

    for _, row in df.iterrows():
        log = simulate_blockchain_log(row['System'], row['Event'])
        blockchain_logs.append(log)

    # Save to CSV as simulated ledger
    ledger_df = pd.DataFrame(blockchain_logs)
    ledger_df['timestamp_readable'] = ledger_df['timestamp'].apply(lambda t: datetime.fromtimestamp(t).isoformat())
    ledger_df.to_csv("simulated_blockchain_ledger.csv", index=False)
    print("Simulated blockchain ledger saved to simulated_blockchain_ledger.csv")

if __name__ == "__main__":
    run_blockchain_simulation("ai_anomaly_log.csv")  # Replace with your actual log file

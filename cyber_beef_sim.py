
import simpy
import json
import random
import pandas as pd
from datetime import datetime

# Load configuration
with open("systems_config.json") as f:
    config = json.load(f)

# Data log
log_data = []

class BeefSystem:
    def __init__(self, env, name, dependencies, failure_prob, recovery_time, systems):
        self.env = env
        self.name = name
        self.dependencies = dependencies
        self.failure_prob = failure_prob
        self.recovery_time = recovery_time
        self.systems = systems
        self.failed = False
        self.action = env.process(self.run())

    def is_dependency_failed(self):
        return any(self.systems[dep].failed for dep in self.dependencies)

    def run(self):
        while True:
            yield self.env.timeout(1)
            # Increase failure chance if a dependency is down
            mod_failure_prob = self.failure_prob
            if self.is_dependency_failed():
                mod_failure_prob *= 2.5  # Amplify failure chance if a dependency is down

            if not self.failed and random.random() < mod_failure_prob:
                self.failed = True
                log_data.append({
                    "time": self.env.now,
                    "system": self.name,
                    "event": "FAILED"
                })
                print(f"[{self.env.now}] {self.name} FAILED")
                yield self.env.timeout(self.recovery_time)
                self.failed = False
                log_data.append({
                    "time": self.env.now,
                    "system": self.name,
                    "event": "RECOVERED"
                })
                print(f"[{self.env.now}] {self.name} RECOVERED")

def setup(env, config):
    systems = {}
    for name, props in config.items():
        systems[name] = None  # placeholder to allow full dict reference
    for name, props in config.items():
        systems[name] = BeefSystem(
            env,
            name,
            props["dependencies"],
            props["failure_prob"],
            props["recovery_time"],
            systems
        )
    return systems

# Simulation environment
env = simpy.Environment()
systems = setup(env, config)
simulation_time = 100  # Simulate 100 time units
env.run(until=simulation_time)

# Save log to CSV
df = pd.DataFrame(log_data)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_csv(f"failure_logs_{timestamp}.csv", index=False)
print(f"Simulation complete. Log saved to failure_logs_{timestamp}.csv")

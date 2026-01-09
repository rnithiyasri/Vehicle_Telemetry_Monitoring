import pandas as pd

def detect_anomalies():
    df = pd.read_csv("data/vehicle_data.csv")

    MAX_SPEED = 100
    MAX_ENGINE_TEMP = 95
    MIN_FUEL = 15

    print("=== Anomaly Detection Report ===")

    overspeed = df[df["speed_kmph"] > MAX_SPEED]
    print(f"Overspeed events: {len(overspeed)}")

    overheat = df[df["engine_temp_c"] > MAX_ENGINE_TEMP]
    print(f"Overheating events: {len(overheat)}")

    low_fuel = df[df["fuel_level_percent"] < MIN_FUEL]
    print(f"Low fuel warnings: {len(low_fuel)}")

    # ✅ COPY THESE LINES HERE ⬇⬇⬇
    overspeed.to_csv("data/overspeed_events.csv", index=False)
    overheat.to_csv("data/overheat_events.csv", index=False)
    low_fuel.to_csv("data/low_fuel_events.csv", index=False)

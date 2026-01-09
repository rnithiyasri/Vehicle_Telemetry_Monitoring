import pandas as pd

def run_analysis():
    df = pd.read_csv("data/vehicle_data.csv")

    print("\n=== Vehicle Data Analysis ===")

    print(f"Total Records: {len(df)}")
    print(f"Average Speed: {round(df['speed_kmph'].mean(), 2)} km/h")

    slow = len(df[df["speed_kmph"] < 40])
    normal = len(df[(df["speed_kmph"] >= 40) & (df["speed_kmph"] <= 80)])
    fast = len(df[df["speed_kmph"] > 80])

    print(f"Slow: {slow}")
    print(f"Normal: {normal}")
    print(f"Fast: {fast}")

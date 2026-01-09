import pandas as pd

def generate_report():
    df = pd.read_csv("data/vehicle_data.csv")

    print("\n=== Summary Report ===")
    print(f"Max Speed: {df['speed_kmph'].max()} km/h")
    print(f"Min Fuel Level: {df['fuel_level_percent'].min()} %")
    print(f"Avg Engine Temp: {round(df['engine_temp_c'].mean(), 2)} °C")

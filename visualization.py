import matplotlib
matplotlib.use("Agg")

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    conn = sqlite3.connect("vehicle_telemetry.db")
    df = pd.read_sql_query("SELECT * FROM telemetry", conn)
    conn.close()

    plt.figure(figsize=(8, 5))
    plt.plot(df["speed"], label="Speed (km/h)")
    plt.axhline(100, linestyle="--", label="Speed Limit")
    plt.xlabel("Time Index")
    plt.ylabel("Speed")
    plt.title("Vehicle Speed Over Time")
    plt.legend()
    plt.tight_layout()

    plt.savefig("telemetry_report.png")
    plt.close()

    print("Graph saved as telemetry_report.png")

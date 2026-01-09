from src.database import create_table
from src.data_generator import generate_vehicle_data
from src.visualization import visualize_data
import sqlite3

print("🚗 Starting Vehicle Telemetry Monitoring System\n")

# Step 1: Initialize database
create_table()

# Step 2: Generate telemetry data
generate_vehicle_data(100)

# Step 3: Simple analysis
conn = sqlite3.connect("vehicle_telemetry.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM telemetry")
total_records = cursor.fetchone()[0]

cursor.execute("SELECT AVG(speed) FROM telemetry")
avg_speed = cursor.fetchone()[0]

cursor.execute("SELECT MAX(speed) FROM telemetry")
max_speed = cursor.fetchone()[0]

cursor.execute("SELECT MIN(fuel) FROM telemetry")
min_fuel = cursor.fetchone()[0]

cursor.execute("SELECT AVG(engine_temp) FROM telemetry")
avg_temp = cursor.fetchone()[0]

conn.close()

print("=== Vehicle Data Analysis ===")
print(f"Total Records: {total_records}")
print(f"Average Speed: {avg_speed:.2f} km/h")

print("\n=== Summary Report ===")
print(f"Max Speed: {max_speed} km/h")
print(f"Min Fuel Level: {min_fuel} %")
print(f"Avg Engine Temp: {avg_temp:.2f} °C")

# Step 4: Visualization
visualize_data()

print("\n✅ System Execution Completed Successfully")

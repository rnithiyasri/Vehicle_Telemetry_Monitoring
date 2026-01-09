import random
from src.database import insert_data

def generate_vehicle_data(records=100):
    print("Vehicle telemetry data generated successfully!")

    for _ in range(records):
        speed = random.randint(30, 120)
        fuel = random.randint(5, 100)
        engine_temp = random.randint(60, 120)

        insert_data(speed, fuel, engine_temp)

import random
import json
from datetime import datetime, timedelta

# Funkcja do generowania losowych dat
def random_date(start_year=2000, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d.%m.%Y")

# Funkcja do generowania danych technicznych
def generate_transport_data(num_entries):
    transport_data = {}
    for i in range(num_entries):
        reg_number = f'{random.randint(1000000000, 9999999999)}'  # Losowy numer rejestracyjny
        manufacturing_date = random_date(1970, 2020)
        registration_date = random_date(2020, 2024)
        tech_in_dates = [random_date(2020, 2024) for _ in range(random.randint(3, 6))]
        transport_data[reg_number] = {
            "manufacturing_date": manufacturing_date,
            "registration_date": registration_date,
            "tech_in_dates": sorted(tech_in_dates, reverse=True)
        }
    return transport_data

# Generowanie danych dla różnych typów pojazdów
automobile_data = generate_transport_data(120)
truck_data = generate_transport_data(56)
ship_data = generate_transport_data(3)
aviation_data = generate_transport_data(5)
bicycle_data = generate_transport_data(1)

# Zapisywanie danych do plików JSON
with open('automobile.json', 'w') as f:
    json.dump(automobile_data, f, indent=4)

with open('truck.json', 'w') as f:
    json.dump(truck_data, f, indent=4)

with open('ship.json', 'w') as f:
    json.dump(ship_data, f, indent=4)

with open('plane.json', 'w') as f:
    json.dump(aviation_data, f, indent=4)

with open('bicycle.json', 'w') as f:
    json.dump(bicycle_data, f, indent=4)

print("Pliki JSON zostały wygenerowane.")

import random
import json
from datetime import datetime, timedelta

# Definicje marek i modeli
producer_osobowe = ["Toyota","Volkswagen","Mercedes-Benz","BMW","Honda","Ford","Audi","Hyundai","Nissan","Chevrolet"]
modele_osobowe = ["elektryczny","sport","SUV","sedan","luks"]

producer_ciezarowe = ["Volvo Trucks","Scania","Mercedes-Benz Trucks","MAN","DAF",
                   "Iveco","Freightliner","Kenworth","Peterbilt","Renault Trucks"]
modele_ciezarowe = ["elektryczny","miejskie","regionalne","długodystansowe"]

producer_statki = ["Navantia", "Fincantieri", "MHI"]
modele_statki = ["kontenerowiec","masowiec","pasażerski"]

producer_samoloty= ["Boeing","Airbus","Embraer","Cessna","Antonov"]
modele_samoloty = ["regionalny","szerokokadłubowy","wąskokadłubowy","transportowy"]

producer_rower = ["HARO"]
model_rower = ["Dirt/Street"]

# Funkcja losująca rok produkcji i datę użytkowania
def losuj_date():
    rok_produkcji = random.randint(1990, 2024)
    start_date = datetime(rok_produkcji, 1, 1)
    end_date = datetime.now()
    losowa_data = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return rok_produkcji, losowa_data.strftime("%Y-%m-%d")

# Funkcja generująca listę pojazdów
def generuj_pojazdy(id, producer, modele, liczba_powtarzan):
    pojazdy = []
    for _ in range(liczba_powtarzan):
        id = random.randint(100000000, 999999999)
        marka = random.choice(producer)
        model = random.choice(modele)
        rok, data = losuj_date()
        pojazdy.append({
            "ID": id,
            "producer": marka,
            "model": model,
            "rok_produkcji": rok,
            "data_przeglądu": data
        })
    return pojazdy

# Generowanie danych
pojazdy_osobowe = generuj_pojazdy(id, producer_osobowe, modele_osobowe, 120)
pojazdy_ciezarowe = generuj_pojazdy(id, producer_ciezarowe, modele_ciezarowe, 56)
statki = generuj_pojazdy(id, producer_statki, modele_statki, 3)
samoloty = generuj_pojazdy(id, producer_samoloty, modele_samoloty, 5)
rowery = generuj_pojazdy(id, producer_rower, model_rower, 1)

# Łączenie wyników
wszystkie_pojazdy = {
    "samochody_osobowe": pojazdy_osobowe,
    "samochody_ciezarowe": pojazdy_ciezarowe,
    "statki": statki,
    "samoloty": samoloty,
    "rowery": rowery
}

# Zapis do pliku JSON
with open("pojazdy.json", "w") as file:
    json.dump(wszystkie_pojazdy, file, indent=4)

print("Wygenerowano dane i zapisano do pojazdy.json")

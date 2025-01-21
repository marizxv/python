from datetime import *
import json
import random

class Pojazd:
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu):
        self.id_pojazdu = id_pojazdu
        self.producer = producer
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.ostatni_przeglad = datetime.strptime(ostatni_przeglad, "%Y-%m-%d")
        self.interwal_przegladu = timedelta(days=interwal_przegladu)

    def czy_wymagany_przeglad(self):
        return datetime.now() >= self.ostatni_przeglad + self.interwal_przegladu

class SomochodOsobowy(Pojazd):
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu):
        super().__init__(id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu)

class SomochodCiezarowy(Pojazd):
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu):
        super().__init__(id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu)

class StatekOceaniczny(Pojazd):
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu):
        super().__init__(id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu)

class Samolot(Pojazd):
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu, kod_statku):
        super().__init__(id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu)
        self.lod_statku = kod_statku

class Rower(Pojazd):
    def __init__(self, id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu):
        super().__init__(id_pojazdu, producer, model, rok_produkcji, ostatni_przeglad, interwal_przegladu)

# Funkcja do tworzenia obiektów pojazdów
def utworz_pojazdy(dane):
    pojazdy = {
        "samochody_osobowe": [],
        "samochody_ciezarowe": [],
        "statki": [],
        "samoloty": [],
        "rowery": []
    }

    for kategoria, lista in dane.items():
        for pojazd in lista:
            interwal = 915  # Zakres interwału przeglądu
            if kategoria == "samochody_osobowe":
                pojazdy[kategoria].append(SomochodOsobowy(pojazd["ID"], pojazd["producer"], pojazd["model"],
                                                          pojazd["rok_produkcji"], pojazd["data_przeglądu"], interwal))
            elif kategoria == "samochody_ciezarowe":
                pojazdy[kategoria].append(SomochodCiezarowy(pojazd["ID"], pojazd["producer"], pojazd["model"],
                                                            pojazd["rok_produkcji"], pojazd["data_przeglądu"], interwal))
            elif kategoria == "statki":
                pojazdy[kategoria].append(StatekOceaniczny(pojazd["ID"], pojazd["producer"], pojazd["model"],
                                                           pojazd["rok_produkcji"], pojazd["data_przeglądu"], interwal))
            elif kategoria == "samoloty":
                kod_statku = f"FL{random.randint(1000, 9999)}"
                pojazdy[kategoria].append(Samolot(pojazd["ID"], pojazd["producer"], pojazd["model"],
                                                  pojazd["rok_produkcji"], pojazd["data_przeglądu"], interwal, kod_statku))
            elif kategoria == "rowery":
                pojazdy[kategoria].append(Rower(pojazd["ID"], pojazd["producer"], pojazd["model"],
                                                pojazd["rok_produkcji"], pojazd["data_przeglądu"], interwal))
    return pojazdy

# Odczyt danych z pliku JSON
with open('pojazdy.json') as file:
    pojazdy_data = json.load(file)

pojazdy = utworz_pojazdy(pojazdy_data)

# Wyświetlanie pojazdów z kategoriami
for kategoria, lista_pojazdow in pojazdy.items():
    print(f"\n{kategoria.capitalize()}:")
    for pojazd in lista_pojazdow:
        status = "WYMAGA PRZEGLĄDU!" if pojazd.czy_wymagany_przeglad() else "Przegląd nie jest wymagany."
        print(f"Pojazd ID: {pojazd.id_pojazdu}, Producer: {pojazd.producer}, "
              f"Model: {pojazd.model}, Rok produkcji: {pojazd.rok_produkcji} \n-> {status}")

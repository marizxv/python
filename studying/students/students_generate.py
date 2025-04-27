import random
import json

universytety_lista = ["Uniwersytet Śląski", "Politechnika Łódzka"]
przedmioty_lista = [
    ["Matematyka", "Matematyka dyskretna", "Analiza matematyczna", "Geometria analityczna", "Informatyka", "Programowanie", "Logika", "Systemy operacyjne"],
    ["Matematyka", "Informatyka", "Programowanie", "Logika", "Systemy operacyjne", "Język angielski", "Filozofia", "Religia", "Gospodarka"]
]
kraje_wymiany_lista = [
    ["Francja", "Niemcy","Belgia"],
    ["Estonia", "Austria"]
]
glowny_kierunek_lista = ["Informatyka", "Matematyka"]
nazwiska_lista = ["Nowak",
                 "Kowalski",
                 "Wiśniewski",
                 "Wójcik",
                 "Kowalczyk",
                 "Kamiński",
                 "Lewandowski",
                 "Zieliński",
                 "Szymański",
                 "Woźniak",
                 "Dąbrowski",
                 "Kozłowski",
                 "Jankowski",
                 "Mazur",
                 "Kwiatkowski",
                 "Wojciechowski",
                 "Krawczyk",
                 "Piotrowski",
                 "Grabowski",
                 "Zając",
                 "Pawłowski",
                 "Michalski",
                 "Król",
                 "Wieczorek",
                 "Jabłoński",
                 "Adamczyk",
                 "Dudek",
                 "Zalewski",
                 "Pająk",
                 "Tomaszewski"]
imiona_lista = ["Adam",
              "Andrzej",
              "Bartosz",
              "Błażej",
              "Damian",
              "Daniel",
              "Dawid",
              "Dominik",
              "Emil",
              "Filip",
              "Grzegorz",
              "Hubert",
              "Jakub",
              "Jan",
              "Jerzy",
              "Kamil",
              "Karol",
              "Krzysztof",
              "Łukasz",
              "Maciej",
              "Marek",
              "Marcin",
              "Michał",
              "Mikołaj",
              "Paweł",
              "Piotr",
              "Rafał",
              "Sebastian",
              "Szymon",
              "Tomasz"]
students = []

for i in range(100):
    imie_index = random.randint(0, len(imiona_lista) - 1) # .randint - integer random value
    nazwisko_index = random.randint(0, len(nazwiska_lista) - 1) # len() - list elements count, -1 because we start from 0
    universytet_index = random.randint(0, len(universytety_lista) - 1)
    progres = []

    data_urodzenia_dzien = random.randint(1, 28)
    data_urodzenia_dzien = str(data_urodzenia_dzien) if data_urodzenia_dzien > 9 else "0" + str(data_urodzenia_dzien) #adding 0 before digit
    data_urodzenia_miesiac = random.randint(1, 12)
    data_urodzenia_miesiac = str(data_urodzenia_miesiac) if data_urodzenia_miesiac > 9 else "0" + str(data_urodzenia_miesiac)
    data_urodzenia_rok = str(random.randint(1999, 2005)) # str() - convert integer to string
    urodziny = data_urodzenia_dzien + '.' + data_urodzenia_miesiac + '.' + data_urodzenia_rok #string concatenation

    for subject in przedmioty_lista[universytet_index]:
        progres.append(random.randint(25, 100))

    student = {
        "imie" : imiona_lista[imie_index],
        "nazwisko" : nazwiska_lista[nazwisko_index],
        "plec" : "mężczyzna",
        "data_urodzenia": urodziny,
        "pesel": random.randint(1000000000, 9999999999),
        "university_type": "Uniwersytet",
        "university_name" : universytety_lista[universytet_index],
        "university_glowny_kierunek" : glowny_kierunek_lista[universytet_index],
        "university_kraje_wymiany" : kraje_wymiany_lista[universytet_index],
        "university_subjects" : przedmioty_lista[universytet_index],
        "progress" : progres,
    }

    print(student)
    students.append(student)

    students_data = open("students.json", "w")
    json.dump(students, students_data, indent = 4) # PyCharm shows error on "students_data", this is PyCharm known bug

    students_data.close()


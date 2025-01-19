import random
import json

universities_list = ["Uniwersytet Śląski", "Politechnika Łódzka"]
subjects_list = [
    ["Matematyka", "Matematyka dyskretna", "Analiza matematyczna", "Geometria analityczna", "Informatyka", "Programowanie", "Logika", "Systemy operacyjne"],
    ["Matematyka", "Informatyka", "Programowanie", "Logika", "Systemy operacyjne", "Język angielski", "Filozofia", "Religia", "Gospodarka"]
]
kraje_wymiany_list = [
    ["Francja", "Niemcy","Belgia"],
    ["Estonia", "Austria"]
]
glowny_kierunek_list = ["Informatyka", "Matematyka"]
surnames_list = ["Nowak",
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
names_list = ["Adam",
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
    name_index = random.randint(0, len(names_list) - 1) # .randint - integer random value
    surname_index = random.randint(0, len(surnames_list) - 1) # len() - list elements count, -1 because we start from 0
    university_index = random.randint(0, len(universities_list) - 1)
    progress = []

    birth_date_day = random.randint(1, 28)
    birth_date_day = str(birth_date_day) if birth_date_day > 9 else "0" + str(birth_date_day) #adding 0 before digit
    birth_date_month = random.randint(1, 12)
    birth_date_month = str(birth_date_month) if birth_date_month > 9 else "0" + str(birth_date_month)
    birth_date_year = str(random.randint(1999, 2005)) # str() - convert integer to string
    birth_date = birth_date_day + '.' + birth_date_month + '.' + birth_date_year #string concatenation

    for subject in subjects_list[university_index]:
        progress.append(random.randint(25, 100))

    student = {
        "imie" : names_list[name_index],
        "nazwisko" : surnames_list[surname_index],
        "plec" : "mężczyzna",
        "data_urodzenia": birth_date,
        "pesel": random.randint(1000000000, 9999999999),
        "university_type": "Uniwersytet",
        "university_name" : universities_list[university_index],
        "university_glowny_kierunek" : glowny_kierunek_list[university_index],
        "university_kraje_wymiany" : kraje_wymiany_list[university_index],
        "university_subjects" : subjects_list[university_index],
        "progress" : progress,
    }

    print(student)
    students.append(student)

    students_data = open("students.json", "w")
    json.dump(students, students_data, indent = 4) # PyCharm shows error on "students_data", never mind, this is PyCharm known bug
                                                   # indent = 4 - this is only for you, Mari, look at the json file itself with and without the parameter
    students_data.close()

#random.randint(0,10)
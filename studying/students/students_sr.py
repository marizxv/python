import json

class Czlowiek:
    imie = None
    nazwisko = None
    dataUrodzenia = None
    plec = None
    pesel = None
    def __init__(self, imie, nazwisko, data_urodzenia, plec, pesel):
        Czlowiek.imie = imie
        Czlowiek.nazwisko = nazwisko
        Czlowiek.data_urodzenia = data_urodzenia
        Czlowiek.plec = plec
        Czlowiek.pesel = pesel

class Uczelnia1:
    nazwa = "Uniwersytet Śląski"
    rodzaj_uczelni = None
    glowny_kierunek = None
    przedmioty = []
    cos_unikatowe = None
    def __init__(self, rodzaj_uczelni, glowny_kierunek, przedmioty, cos_unikatowe):
        Uczelnia1.rodzaj_uczelni = rodzaj_uczelni
        Uczelnia1.glowny_kierunek = glowny_kierunek
        Uczelnia1.przedmioty = przedmioty
        Uczelnia1.cos_unikatowe = cos_unikatowe

class Uczelnia2:
    nazwa = "Politechnika Łódzka"
    rodzaj_uczelni = None
    glowny_kierunek = None
    przedmioty = []
    inne_unikatowe = None
    def __init__ (self, rodzaj_uczelni, glowny_kierunek, przedmioty, inne_unikatowe):
        Uczelnia2.rodzaj_uczelni = rodzaj_uczelni
        Uczelnia2.glowny_kierunek = glowny_kierunek
        Uczelnia2.przedmioty = przedmioty
        Uczelnia2.inne_unikatowe = inne_unikatowe

class Student(Czlowiek, Uczelnia1, Uczelnia2):
    postep = {}
    def __init__(self, imie, nazwisko, data_urodzenia, plec, pesel, uczelnia, postep = None):

        Czlowiek.__init__(self, imie, nazwisko, data_urodzenia, plec, pesel)

        if len(uczelnia) == 2:
            Uczelnia1.__init__(self, uczelnia[0][1], uczelnia[0][2], uczelnia[0][3], 'Mam wieczory pizzy!')
            Uczelnia2.__init__(self, uczelnia[1][1], uczelnia[1][2], uczelnia[1][3], 'A ja nie mam, ale nie szkodzi!')
        elif uczelnia[0] == Uczelnia1.nazwa:
            Uczelnia1.__init__(self, uczelnia[1], uczelnia[2], uczelnia[3], 'Mam wieczory pizzy!')
            Uczelnia2.__init__(self, None, None, [], None)
        elif uczelnia[0] == Uczelnia2.nazwa:
            Uczelnia1.__init__(self, None, None, [], None)
            Uczelnia2.__init__(self, uczelnia[1], uczelnia[2], uczelnia[3], 'A ja nie mam, ale nie szkodzi!')

        if len(Uczelnia1.przedmioty) > 0 and len(Uczelnia2.przedmioty) > 0:
            Student.set_postep(self, Uczelnia1, postep[0])
            Student.set_postep(self, Uczelnia2, postep[1])
        elif len(Uczelnia1.przedmioty) > 0:
            Student.set_postep(self, Uczelnia1, postep)
            Student.postep.pop(Uczelnia2.nazwa, None)
        elif len(Uczelnia2.przedmioty) > 0:
            Student.set_postep(self, Uczelnia2, postep)
            Student.postep.pop(Uczelnia1.nazwa, None)
        else:
            Student.postep.pop(Uczelnia1.nazwa, None)
            Student.postep.pop(Uczelnia2.nazwa, None)

    def set_postep(self, Uczelnia, postep):
        Student.postep[Uczelnia.nazwa] = []
        for index, przedmiot in enumerate(Uczelnia.przedmioty):
            Student.postep[Uczelnia.nazwa].append({przedmiot: postep[index]})
    def get_postep(self):
        return Student.postep


# opening JSON file
students_data_json = open('students.json')
# returns JSON object as a list
students_data = json.load(students_data_json)
# closing JSON file
students_data_json.close()

for student_info in students_data:
    student = Student(
        student_info["imie"],
        student_info["nazwisko"],
        student_info["data_urodzenia"],
        student_info["plec"],
        student_info["pesel"],
        [student_info["university_name"], student_info["university_type"],
                 student_info["university_glowny_kierunek"], student_info["university_subjects"]],
        student_info["progress"]
    )
    print(f"{student.imie}, {student.nazwisko}, {student.data_urodzenia}")
    for uni, przedmioty in student.get_postep().items():
        print(f"Uczelnia: {uni}")
        for przedmiot_ocena in przedmioty:
            for przedmiot, ocena in przedmiot_ocena.items():
                print(f" - {przedmiot}: {ocena}%")
    print("=" * 50)



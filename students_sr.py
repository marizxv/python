class Czlowiek:
    imie = None
    nazwisko = None
    dataUrodzenia = None
    plec = None
    pesel = None
    def __init__(self, imie, nazwisko, dataUrodzenia, plec, pesel):
        Czlowiek.imie = imie
        Czlowiek.nazwisko = nazwisko
        Czlowiek.dataUrodzenia = dataUrodzenia
        Czlowiek.plec = plec
        Czlowiek.pesel = pesel

class Uczelnia1:
    nazwa = None
    rodzajUczelni = None
    glownyKierunek = None
    krajeWymianyStudentow = None
    def __init__(self, nazwa, rodzajUczelni, glownyKierunek, krajeWymianyStudentow):
        Uczelnia1.nazwa = nazwa
        Uczelnia1.rodzajUczelni = rodzajUczelni
        Uczelnia1.glownyKierunek = glownyKierunek
        Uczelnia1.krajeWymianyStudentow = krajeWymianyStudentow

class Uczelnia2:
    nazwa = None
    rodzajUczelni = None
    glownyKierunek = None
    def __init__ (self, nazwa, rodzajUczelni, glownyKierunek):
        Uczelnia2.nazwa = nazwa
        Uczelnia2.rodzajUczelni = rodzajUczelni
        Uczelnia2.glownyKierunek = glownyKierunek

class Student(Czlowiek, Uczelnia1, Uczelnia2):
    def __init__(self, imie, nazwisko, dataUrodzenia, plec, pesel, uczelnia1=None, uczelnia2=None):
        # Inicjalizacja klasy Czlowiek
        Czlowiek.__init__(self, imie, nazwisko, dataUrodzenia, plec, pesel)
        # Inicjalizacja klasy Uczelnia1
        if uczelnia2 is None:
            uczelnia2 = []
        if uczelnia1 is None:
            uczelnia1 = []
        if len(uczelnia1) == 4:
            Uczelnia1.__init__(self, uczelnia1[0], uczelnia1[1], uczelnia1[2], uczelnia1[3])
        else:
            Uczelnia1.__init__(self, None, None, None, None)
        # Inicjalizacja klasy Uczelnia2
        if len(uczelnia2) == 3:
            Uczelnia2.__init__(self, uczelnia2[0], uczelnia2[1], uczelnia2[2])
        else:
            Uczelnia2.__init__(self, None, None, None)

    def get_ucz1(self):
        return Uczelnia1.nazwa, Uczelnia1.rodzajUczelni, Uczelnia1.glownyKierunek, Uczelnia1.krajeWymianyStudentow

    def get_ucz2(self):
        return Uczelnia2.nazwa, Uczelnia2.rodzajUczelni, Uczelnia2.glownyKierunek

    def get_uczelnia(self):
        uczelnia1 = self.get_ucz1()
        uczelnia2 = self.get_ucz2()
        # print(uczelnia1, uczelnia2)
        # print(uczelnia1[0], uczelnia2[0])
        if uczelnia1[0] and uczelnia2[0]:
            return Czlowiek.imie, uczelnia1, uczelnia2
        elif  uczelnia1[0]:
            return Czlowiek.imie, uczelnia1
        else:
            return Czlowiek.imie, uczelnia2



# Tworzenie obiektu klasy Student
student1 = Student(
    "Marek",
    "Tomaszewski",
    "1988-12-12",
    "mężczyzna",
    "01234567890",
    ["Uniwersytet Śląski","Uniwersytet","Matematyka", ["Francja", "Niemcy"]],
    ["Politechnika Łódzka","Politechnika","Inżynieria"]
)

print(student1.get_uczelnia())

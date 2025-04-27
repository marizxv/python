import datetime
import json

class Transport:
    __registration_number = None
    __manufacturing_date = None
    __registration_date = None
    __tech_in_dates = []
    __last_tech_in_days = 0
    __DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, registration_number):
        transport_type = self.get_transport_type()         # Dynamiczne otwieranie pliku w zależności od typu transportu
        db_data_json = open(f'{transport_type}.json')
        transport_data = json.load(db_data_json)
        db_data_json.close()

        if registration_number in transport_data.keys():
            self.__registration_number = registration_number
            self.__manufacturing_date = transport_data[registration_number]['manufacturing_date']
            self.__registration_date = transport_data[registration_number]['registration_date']
            self.__tech_in_dates = transport_data[registration_number]['tech_in_dates']
            self.__tech_in_dates.sort(key=lambda x: datetime.datetime.strptime(x, self.__DATE_FORMAT), reverse=True)
            self.set_last_tech_in_days()
        else:
            print('Invalid registration number', registration_number)

    def set_last_tech_in_days(self):
        last_TI_date = datetime.datetime.strptime(self.__tech_in_dates[0], self.__DATE_FORMAT)
        today = datetime.date.today().strftime(self.__DATE_FORMAT)
        today_date = datetime.datetime.strptime(today, self.__DATE_FORMAT)
        delta = today_date - last_TI_date
        self.__last_tech_in_days = delta.days

    def needs_tech_in(self):
        return self.get_tech_in_period() <= self.__last_tech_in_days

    def print_transport_info(self, number=0):
        indent = '~'
        if number != 0:
            print('#' + str(number))

        print(indent, 'Registration number:\t', self.__registration_number)
        print(indent, 'Manufacturing date:\t', self.__manufacturing_date)
        print(indent, 'Registration date:\t', self.__registration_date)
        print(indent, 'Last Tech In date:\t', self.__tech_in_dates[0])
        print(indent, 'After last Tech In:\t', self.__last_tech_in_days, 'days')
        print(indent, 'Tech In period:\t\t', self.get_tech_in_period(), 'days')

        if self.needs_tech_in():
            needs_tech_in = 'Yes'
        else:
            needs_tech_in = 'No'

        print(indent, 'Tech In needed:\t\t', needs_tech_in)
        print()

    def get_registration_number(self):
        return self.__registration_number

    def get_transport_type(self):
        return ''  # get_transport_type must be overridden in child class

    def get_tech_in_period(self):
        return 0  # get_tech_in_period must be overridden in child class

class Automobile(Transport):
    __TRANSPORT_TYPE = 'automobile'
    __TECH_IN_PERIOD = 365

    def __init__(self, registration_number):
        Transport.__init__(self, registration_number)

    def get_transport_type(self):
        return self.__TRANSPORT_TYPE

    def get_tech_in_period(self):
        return self.__TECH_IN_PERIOD

class Truck(Transport):
    __TRANSPORT_TYPE = 'truck'
    __TECH_IN_PERIOD = 365

    def __init__(self, registration_number):
        Transport.__init__(self, registration_number)

    def get_transport_type(self):
        return self.__TRANSPORT_TYPE

    def get_tech_in_period(self):
        return self.__TECH_IN_PERIOD

class Ship(Transport):
    __TRANSPORT_TYPE = 'ship'
    __TECH_IN_PERIOD = 160

    def __init__(self, registration_number):
        Transport.__init__(self, registration_number)

    def get_transport_type(self):
        return self.__TRANSPORT_TYPE

    def get_tech_in_period(self):
        return self.__TECH_IN_PERIOD

class Plane(Transport):
    __TRANSPORT_TYPE = 'plane'
    __TECH_IN_PERIOD = 30

    def __init__(self, registration_number):
        Transport.__init__(self, registration_number)

    def get_transport_type(self):
        return self.__TRANSPORT_TYPE

    def get_tech_in_period(self):
        return self.__TECH_IN_PERIOD

class Bicycle(Transport):
    __TRANSPORT_TYPE = 'bicycle'
    __TECH_IN_PERIOD = 730

    def __init__(self, registration_number):
        Transport.__init__(self, registration_number)

    def get_transport_type(self):
        return self.__TRANSPORT_TYPE

    def get_tech_in_period(self):
        return self.__TECH_IN_PERIOD

with open('automobile.json', 'r') as file_data:
    auto_reg_numbers_data = json.load(file_data)
    auto_reg_numbers = auto_reg_numbers_data.keys()

print()
print('Automobiles:')
print()

for index, reg_number in enumerate(auto_reg_numbers):
    auto = Automobile(reg_number)
    if auto.get_registration_number():
        auto.print_transport_info(index + 1)

with open('truck.json', 'r') as file_data:
    truck_reg_numbers_data = json.load(file_data)
    truck_reg_numbers = truck_reg_numbers_data.keys()

print('Trucks:')
print()

for index, reg_number in enumerate(truck_reg_numbers):
    truck = Truck(reg_number)
    if truck.get_registration_number():
        truck.print_transport_info(index + 1)

with open('plane.json', 'r') as file_data:
    aviation_reg_numbers_data = json.load(file_data)
    aviation_reg_numbers = aviation_reg_numbers_data.keys()

print('Planes:')
print()

for index, reg_number in enumerate(aviation_reg_numbers):
    plane = Plane(reg_number)
    if plane.get_registration_number():
        plane.print_transport_info(index + 1)

with open('ship.json', 'r') as file_data:
    ship_reg_numbers_data = json.load(file_data)
    ship_reg_numbers = ship_reg_numbers_data.keys()

print('Ships:')
print()

for index, reg_number in enumerate(ship_reg_numbers):
    ship = Ship(reg_number)
    if ship.get_registration_number():
        ship.print_transport_info(index + 1)

with open('bicycle.json', 'r') as file_data:
    bicycle_reg_numbers_data = json.load(file_data)
    bicycle_reg_numbers = bicycle_reg_numbers_data.keys()

print('Bicycle: \nOnly one of a kind')
print()

for index, reg_number in enumerate(bicycle_reg_numbers):
    bicycle = Bicycle(reg_number)
    if bicycle.get_registration_number():
        bicycle.print_transport_info(index + 1)


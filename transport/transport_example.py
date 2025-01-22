import datetime
import json

class Transport:
    TRANSPORT_TYPE = None
    TECH_IN_PERIOD = None
    registration_number = None
    manufacturing_date = None
    registration_date = None
    tech_in_dates = []
    last_tech_in_days = 0
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, registration_number):
        db_data_json = open(self.TRANSPORT_TYPE + '.json')
        transport_data = json.load(db_data_json)
        db_data_json.close()

        if registration_number in transport_data.keys():
            self.registration_number = registration_number
            self.manufacturing_date = transport_data[registration_number]['manufacturing_date']
            self.registration_date = transport_data[registration_number]['registration_date']
            self.tech_in_dates = transport_data[registration_number]['tech_in_dates']
            self.tech_in_dates.sort(key=lambda x: datetime.datetime.strptime(x, self.DATE_FORMAT), reverse=True)
            self.set_last_tech_in_days()
        else:
            print('Invalid registration number', registration_number)

    def set_last_tech_in_days(self):
        last_TI_date = datetime.datetime.strptime(self.tech_in_dates[0], self.DATE_FORMAT)
        today = datetime.date.today().strftime(self.DATE_FORMAT)
        today_date = datetime.datetime.strptime(today, self.DATE_FORMAT)
        delta = today_date - last_TI_date
        self.last_tech_in_days = delta.days

    def needs_tech_in(self):
        return self.TECH_IN_PERIOD <= self.last_tech_in_days

    def print_transport_info(self, number = 0):
        indent = '~'
        if number == 0:
            print(indent, 'Registration number:      ', self.registration_number)
        else:
            print(number, 'Registration number:      ', self.registration_number)

        print(indent, 'Manufacturing date:       ', self.manufacturing_date)
        print(indent, 'Registration date:        ', self.manufacturing_date)
        print(indent, 'Last Tech In date:        ', self.tech_in_dates[0])
        print(indent, 'After last Tech In:       ', self.last_tech_in_days, 'days')
        print(indent, 'Tech In period:           ', self.TECH_IN_PERIOD, 'days')

        if self.needs_tech_in():
            needs_tech_in = 'Yes'
        else:
            needs_tech_in = 'No'

        print(indent, 'Tech In needed:           ', needs_tech_in)
        print()

class Automobile(Transport):
    TRANSPORT_TYPE = 'automobile'
    TECH_IN_PERIOD = 365

class Boat(Transport):
    TRANSPORT_TYPE = 'boat'
    TECH_IN_PERIOD = 160

class Plain(Transport):
    TRANSPORT_TYPE = 'plain'
    TECH_IN_PERIOD = 30

auto_reg_numbers = ['1111111111', '1111111112', '1111111113']
plain_reg_numbers = ['2111111111', '2111111112', '2111111113']
boat_reg_numbers = ['3111111111', '3111111112', '3111111113']

print()
print('Automobiles:')
print()

for index, reg_number in enumerate(auto_reg_numbers):
    auto = Automobile(reg_number)
    if auto.registration_number:
        auto.print_transport_info(index + 1)

print('Plains:')
print()

for index, reg_number in enumerate(plain_reg_numbers):
    plain = Plain(reg_number)
    if plain.registration_number:
        plain.print_transport_info(index + 1)

print('Boats:')
print()

for index, reg_number in enumerate(boat_reg_numbers):
    boat = Boat(reg_number)
    if boat.registration_number:
        boat.print_transport_info(index + 1)
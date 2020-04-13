from states import *
from mimesis import Person as MimPerson
from mimesis.enums import Gender as MimGender


class Event:
    def __init__(self, amount_countries, text, probability=0):
        self.__text = text
        self.__amount_countries = amount_countries
        self.__probability = probability
        self.__countries = set()
        self.__conditions = ''
        self.__effects = ''

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_amount_countries(self):
        return self.__amount_countries

    def set_amount_countries(self, amount):
        self.__amount_countries = amount

    def get_probability(self):
        return self.__probability

    def set_probability(self, value):
        self.__probability = value

    def get_conditions(self):
        return self.__conditions

    def set_conditions(self, conditions):
        self.__conditions = conditions

    def fill_in_text(self, countries):
        result = []
        text = self.get_text()
        countries = list(countries)
        if self.get_amount_countries() == 1:
            person1 = MimPerson(list(countries[0].get_languages())[0])
            text = str.replace(text, '<man1>', person1.full_name(gender=MimGender.MALE))
            text = str.replace(text, '<woman1>', person1.full_name(gender=MimGender.FEMALE))

            text = str.replace(text, '<country1>', countries[0].get_name())
            text = str.replace(text, '<countrian1>', countries[0].get_conj())
            text = str.replace(text, '<ruler1>', countries[0].get_ruler().full_name())
            text = str.replace(text, '<cap1>', countries[0].get_capital())
            text = str.replace(text, '<rulertype1>', countries[0].get_ruler_type())
            text = str.replace(text, '<supplycenter1>', countries[0].random_supply_center().get_name())
            if countries[0].non_supply_centers():
                text = str.replace(text, '<nonsupplycenter1>', countries[0].random_non_supply_center().get_name())
            text = str.replace(text, '<province1>', countries[0].random_province().get_name())

        if self.get_amount_countries() == 2:
            person2 = MimPerson(list(countries[1].get_languages())[0])
            text = str.replace(text, '<man2>', person2.full_name(gender=MimGender.MALE))
            text = str.replace(text, '<woman2>', person2.full_name(gender=MimGender.FEMALE))

            text = str.replace(text, '<country2>', countries[1].get_name())
            text = str.replace(text, '<countrian2>', countries[1].get_conj())
            text = str.replace(text, '<ruler2>', countries[1].get_ruler().full_name())
            text = str.replace(text, '<cap2>', countries[1].get_capital())
            text = str.replace(text, '<rulertype2>', countries[1].get_ruler_type())
            text = str.replace(text, '<supplycenter2>', countries[1].random_supply_center().get_name())
            if countries[1].non_supply_centers():
                text = str.replace(text, '<nonsupplycenter2>', countries[1].random_non_supply_center().get_name())
            text = str.replace(text, '<province2>', countries[1].random_province().get_name())

        if self.get_amount_countries() == 3:
            person3 = MimPerson(list(countries[2].get_languages())[0])
            text = str.replace(text, '<man3>', person3.full_name(gender=MimGender.MALE))
            text = str.replace(text, '<woman3>', person3.full_name(gender=MimGender.FEMALE))

            text = str.replace(text, '<country3>', countries[2].get_name())
            text = str.replace(text, '<countrian3>', countries[2].get_conj())
            text = str.replace(text, '<ruler3>', countries[2].get_ruler().full_name())
            text = str.replace(text, '<cap3>', countries[2].get_capital())
            text = str.replace(text, '<rulertype3>', countries[2].get_ruler_type())
            text = str.replace(text, '<supplycenter3>', countries[2].random_supply_center().get_name())
            if countries[2].non_supply_centers():
                text = str.replace(text, '<nonsupplycenter3>', countries[2].random_non_supply_center().get_name())
            text = str.replace(text, '<province3>', countries[2].random_province().get_name())

        if self.get_amount_countries() == 4:
            person4 = MimPerson(list(countries[3].get_languages())[0])
            text = str.replace(text, '<man4>', person4.full_name(gender=MimGender.MALE))
            text = str.replace(text, '<woman4>', person4.full_name(gender=MimGender.FEMALE))

            text = str.replace(text, '<country4>', countries[3].get_name())
            text = str.replace(text, '<countrian4>', countries[3].get_conj())
            text = str.replace(text, '<ruler4>', countries[3].get_ruler().full_name())
            text = str.replace(text, '<cap4>', countries[3].get_capital())
            text = str.replace(text, '<rulertype4>', countries[3].get_ruler_type())
            text = str.replace(text, '<supplycenter4>', countries[3].random_supply_center().get_name())
            if countries[3].non_supply_centers():
                text = str.replace(text, '<nonsupplycenter4>', countries[3].random_non_supply_center().get_name())
            text = str.replace(text, '<province4>', countries[3].random_province().get_name())

        return text

    def get_effects(self):
        return self.__effects

    def set_effects(self, effects):
        self.__effects = effects







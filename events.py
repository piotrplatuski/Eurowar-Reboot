from states import *
from mimesis import Person as MimPerson
from mimesis.enums import Gender as MimGender


class Event:
    def __init__(self, text, amount_countries, probability=0):
        self.__text = text
        self.__amount_countries = amount_countries
        self.__probability = probability
        self.__countries = set()
        self.__conditions = set()

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

        if self.get_amount_countries() == 2:
            person1 = MimPerson(countries[1].get_languages().pop())
            text = str.replace(text, '<man2>', person1.full_name(gender=MimGender.MALE))
            text = str.replace(text, '<woman2>', person1.full_name(gender=MimGender.FEMALE))

            text = str.replace(text, '<country2>', countries[1].get_name())
            text = str.replace(text, '<countrian2>', countries[1].get_conj())
            text = str.replace(text, '<ruler2>', countries[1].get_ruler().full_name())
            text = str.replace(text, '<cap2>', countries[1].get_capital())
        return text

    def fire(self):
        # to be implemented: this is where the effects of the event take place.
        pass





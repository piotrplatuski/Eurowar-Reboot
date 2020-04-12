import random


prices = {"railway": 500}


class Province:
    def __init__(self, code, name="", supply_center=False):
        self.__code = code
        self.__name = name
        self.__supply_center = supply_center
        self.__buildings = set()
        self.__owner = None
        self.__original_owner = None
        self.__bordering = set()

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def has_supply_center(self):
        return self.__supply_center

    def get_buildings(self):
        return self.__buildings

    def add_building(self, building):
        if building not in self.get_buildings()\
                and building in prices.keys():
            self.__buildings.add(building)
            self.__owner.change_balance(-prices[building])

    def get_owner(self):
        return self.__owner

    def add_owner(self, country):
        self.__owner = country

    def add_original_owner(self, country):
        self.__original_owner = country

    def set_onedir_bordering(self, region):
        self.__bordering.add(region)

    def set_bordering(self, regions):
        for region in regions:
            self.__bordering.add(region)
            region.set_onedir_bordering(self)

    def get_bordering_codes(self):
        return {region.get_code() for region in self.__bordering}

    def get_bordering_names(self):
        return {region.get_name() for region in self.__bordering}

    def borders(self, other):
        if other in self.__bordering:
            return True
        else:
            return False


class SeaZone:
    def __init__(self, code, name=''):
        self.__code = code
        self.__name = name
        self.__bordering = set()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_onedir_bordering(self, region):
        self.__bordering.add(region)

    def set_bordering(self, regions):
        for region in regions:
            self.__bordering.add(region)
            region.set_onedir_bordering(self)

    def get_bordering(self):
        return self.__bordering

    def get_bordering_codes(self):
        return {region.get_code() for region in self.get_bordering()}

    def get_bordering_names(self):
        return {region.get_name() for region in self.get_bordering()}

    def borders(self, other):
        if other in self.get_bordering():
            return True
        else:
            return False


class Country:
    def __init__(self, name, conj, balance=0, government="", stability=7):
        self.__name = name
        self.__official_name = ""
        self.__provinces = set()
        self.__cores = set()
        self.__balance = balance
        self.__government = government
        self.__languages = set()
        self.__conj = conj
        self.__ruler = None
        self.__capital = None
        self.__ruler_type = 'Ruler'
        self.__stability = stability

    def get_name(self):
        return self.__name

    def set_official_name(self, name):
        self.__official_name = name

    def get_official_name(self):
        return self.__official_name

    def get_provinces(self):
        return self.__provinces

    def get_provinces_codes(self):
        return {prov.get_code() for prov in self.get_provinces()}

    def get_provinces_names(self):
        return {prov.get_name() for prov in self.get_provinces()}

    def get_cores(self):
        return self.__cores

    def get_cores_codes(self):
        return {prov.get_code() for prov in self.get_cores()}

    def get_cores_names(self):
        return {prov.get_name() for prov in self.get_cores()}

    def get_balance(self):
        return self.__balance

    def add_provinces(self, provinces):
        for province in provinces:
            self.__provinces.add(province)
            province.add_owner(self)

    def add_cores(self, provinces):
        for province in provinces:
            self.__cores.add(province)
            province.add_original_owner(self)

    def change_balance(self, amount):
        self.__balance += amount

    def get_government(self):
        return self.__government

    def set_government(self, government):
        self.__government = government

    def get_buildings(self):
        # to be implemented
        # double iteration with prices.keys?
        for province in self.__provinces:
            return province.get_buildings()

    def borders(self, other):
        for own_prov in self.get_provinces():
            for oth_prov in other.get_provinces():
                if own_prov.borders(oth_prov):
                    return True
        return False

    def get_border_with(self, other):
        result = set()
        for own_prov in self.get_provinces():
            for oth_prov in other.get_provinces():
                if own_prov.borders(oth_prov):
                    result.add((own_prov, oth_prov))
        return result

    def get_border_with_names(self, other):
        result = set()
        coll = self.get_border_with(other)
        while coll:
            current = coll.pop()
            result.add((current[0].get_name(), current[1].get_name()))
        return result

    def get_border_with_codes(self, other):
        result = set()
        coll = self.get_border_with(other)
        while coll:
            current = coll.pop()
            result.add((current[0].get_code(), current[1].get_code()))
        return result

    def get_languages(self):
        return self.__languages

    def set_languages(self, languages):
        self.__languages = languages

    def get_conj(self):
        return self.__conj

    def set_conj(self, conj):
        self.__conj = conj

    def get_ruler(self):
        return self.__ruler

    def set_ruler(self, ruler):
        self.__ruler = ruler

    def get_capital(self):
        return self.__capital

    def set_capital(self, city):
        self.__capital = city

    def get_ruler_type(self):
        return self.__ruler_type

    def set_ruler_type(self, title):
        self.__ruler_type = title

    def get_stability(self):
        return self.__stability

    def change_stability(self, value):
        self.__stability += value

    def missing_attributes(self):
        result = []
        extra = ''
        if self.get_provinces() == set():
            result.append('Provinces')
        if self.get_cores() == set():
            result.append('Cores')
        if self.get_official_name() == '':
            result.append('Official name')
        if self.get_languages() == set():
            result.append('Languages')
        if self.get_ruler() is None:
            result.append('Ruler')
        if self.get_capital() == '':
            result.append('Capital')
        if self.get_ruler_type() == '':
            result.append('Ruler type')
        if self.get_ruler_type() == 'Ruler':
            extra = 'The current ruler type is Ruler. It will work, but you might want to change it for immersion.'

        return 'There are ' + str(len(result)) + ' missing attributes: ' + str(result) + '. ' + extra

    def supply_centers(self):
        return {prov for prov in self.get_provinces() if prov.has_supply_center() is True}

    def non_supply_centers(self):
        return {prov for prov in self.get_provinces() if prov.has_supply_center() is False}

    def random_province(self):
        return random.choice(list(self.get_provinces()))

    def random_supply_center(self):
        return random.choice(list(self.supply_centers()))

    def random_non_supply_center(self):
        return random.choice(list(self.non_supply_centers()))


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__nickname = None
        self.__birthyear = None

    def full_name(self):
        if self.get_nickname() is None:
            return self.__first_name + " " + self.__last_name
        else:
            return self.__first_name + " '" + self.__nickname + "' "  + self.__last_name

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, name):
        self.__first_name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, name):
        self.__last_name = name

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, name):
        self.__nickname = name

    def get_birthyear(self):
        return self.__birthyear

    def set_birthyear(self, year):
        self.__birthyear = year








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
    def __init__(self, name, balance=None, government=""):
        self.__name = name
        self.__official_name = ""
        self.__provinces = set()
        self.__cores = set()
        self.__balance = balance
        self.__government = government

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








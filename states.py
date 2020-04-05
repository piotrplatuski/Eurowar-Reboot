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
        if building not in self.__buildings\
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

    def get_bordering_codes(self):
        return {region.get_code() for region in self.__bordering}

    def get_bordering_names(self):
        return {region.get_name() for region in self.__bordering}

    def borders(self, other):
        if other in self.__bordering:
            return True
        else:
            return False


class Country:
    def __init__(self, name, balance=None, government=""):
        self.__name = name
        self.__provinces = set()
        self.__cores = set()
        self.__balance = balance
        self.__government = government

    def get_name(self):
        return self.__name

    def get_provinces_codes(self):
        return {prov.get_code() for prov in self.__provinces}

    def get_provinces_names(self):
        return {prov.get_name() for prov in self.__provinces}

    def get_cores_codes(self):
        return {prov.get_code() for prov in self.__cores}

    def get_cores_names(self):
        return {prov.get_name() for prov in self.__cores}

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
        # to be implemented
        # for loop
        pass




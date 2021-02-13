############
    # "python.pythonPath": "/Library/Frameworks/Python.framework/Versions/3.9/bin/python3"
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.firstharvest = first_harvest
        self.color = color
        self.isseedless = is_seedless
        self.isbestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)
    
    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'-{pairing}')
        print()




def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    codes = {}
    for melon in melon_types:
        codes[melon.code] = melon
    return codes



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_number, harvester):
        self.melon_type = melon_type
        self.shape_rating = int(shape_rating)
        self.color_rating = int(color_rating)
        self.field_number = int(field_number)
        self.harvester = harvester
    def is_sellable(self):
        if self.shape_rating < 6:
            return False
        elif self.color_rating < 6:
            return False
        elif self.field_number == 3:
            return False
        else:
            return True
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon_1)
    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melons.append(melon_2)
    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melons.append(melon_3)
    melon_4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melons.append(melon_4)
    melon_5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melons.append(melon_5)
    melon_6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melons.append(melon_6)
    melon_7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melons.append(melon_7)
    melon_8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melons.append(melon_8)
    melon_9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')
    melons.append(melon_9)

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable()==True:
            sold_statement = "can be sold"
        elif melon.is_sellable()==False:
            sold_statement = "is not sellable"
        print(f'Harvested by {melon.harvester} from Field {melon.field_number} {sold_statement}')

melon_types = make_melon_types()
print_pairing_info(melon_types)
make_melon_type_lookup(melon_types)   
melons_by_id = make_melon_type_lookup(melon_types)
melons = make_melons(melons_by_id)
get_sellability_report(melons)


from harvest import Melon, MelonType, make_melon_types, make_melon_type_lookup, get_sellability_report

file = open('harvest_log.txt')

melon_types = make_melon_types()
melons_by_id = make_melon_type_lookup(melon_types)

melons = []
for line in file:
    line = line.rstrip()
    tokens = line.split(" ")
    melon = Melon(melons_by_id[tokens[5]],tokens[1],tokens[3],tokens[11],tokens[8])
    melons.append(melon)
get_sellability_report(melons)

    

    
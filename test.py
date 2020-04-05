from american_map import *

mid = Province('MID', 'Middelland')
tex = Province('TEX', 'Texas')
heartland = Country('Heartland', 600, 'republic')
heartland.add_provinces({mid, tex})
heartland.change_balance(800)
mid.add_building('railway')

print(mid.get_buildings())
print(mid.get_owner().get_name())
print(heartland.get_balance())
print(heartland.get_provinces_codes())
print(heartland.get_provinces_names())
print(heartland.get_buildings())

print(peru.get_provinces_names())
print(peru.get_cores_codes())
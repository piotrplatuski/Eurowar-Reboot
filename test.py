from american_map import *
from states import *

mexico.change_balance(4000)
assert mexico.get_balance() == 4000
mex.add_building('railway')
assert mexico.get_balance() == 4000 - prices['railway']

mexico.add_provinces({mia})
print(mexico.get_provinces_names())
print(mexico.get_cores_codes())

mexico.set_government('dictatorship')
assert mexico.get_government() == 'dictatorship'
assert mexico.get_name() == 'Mexico'

mex.set_bordering({ver, oax, gue, gua, pot})
print(pot.get_bordering_names())
pot.set_bordering({mex})
print(mex.get_bordering_codes())
assert mex.borders(ver) is True
assert ver.borders(mex) is True

print(chi.get_bordering_names())
assert new_york.borders(quebec) is True
assert heartland.borders(new_york) is False
assert florida.borders(cuba) is False

quebec.add_provinces({vem})
new_york.add_provinces({mas})
assert vem.borders(mas) is True

print('________')
print(heartland.get_border_with(quebec))
print(new_york.get_border_with_names(quebec))
print(heartland.get_border_with_codes(quebec))
print(new_york.get_border_with_codes(quebec))
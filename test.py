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
from states import Province, Country

# BRITISH COLUMBIA
anc = Province('anc', 'Anchorage', True)
cgy = Province('cgy', 'Calgary', True)
nbc = Province('nbc', 'Northern British-Columbia', False)
van = Province('van', 'Vancouver', True)
yuk = Province('yuk', 'Yukon', False)

british_columbia = Country('British Columbia', 0, 'republic')
bc_start_provs = {anc, cgy, nbc, van, yuk}
british_columbia.add_cores(bc_start_provs)
british_columbia.add_provinces(bc_start_provs)

# QUEBEC
abi = Province('abi', 'Abitibi', False)
bea = Province('bea', 'Beauce', False)
cot = Province('cot', 'Cote-Nord', False)
gas = Province('gas', 'Gaspesie', False)
mon = Province('mon', 'Montreal', True)
que = Province('que', 'Quebec', True)
ung = Province('ung', 'Ungava', True)

quebec = Country('Quebec', 0, 'republic')
que_start_provs = {abi, bea, cot, gas, mon, que, ung}
quebec.add_cores(que_start_provs)
quebec.add_provinces(que_start_provs)

# REST OF CANADA + GREENLAND
gre = Province('gre', 'Greenland', True)
lab = Province('lab', 'Labrador', False)
man = Province('man', 'Manitoba', True)
nbr = Province('nbr', 'New Brunswick', False)
nfl = Province('nfl', 'Newfoundland', False)
non = Province('non', 'Northern Ontario', False)
nsc = Province('nsc', 'Nova Scotia', True)
nun = Province('nun', 'Nunavut', False)
nwt = Province('nwt', 'North West Territories', False)
ont = Province('ont', 'Ontario', True)
sas = Province('sas', 'Saskatchewan', False)
won = Province('won', 'Western Ontario', False)

# CALIFORNIA
los = Province('los', 'Los Angeles', True)
sdi = Province('sdi', 'San Diego', True)
sfi = Province('sfi', 'San Francisco', True)

california = Country('California', 0, 'republic')
cal_start_provs = {los, sdi, sfi}
california.add_cores(cal_start_provs)
california.add_provinces(cal_start_provs)


# TEXAS
dal = Province('dal', 'Dallas', True)
hou = Province('hou', 'Houston', True)
san = Province('san', 'San Antonio', True)
wte = Province('wte', 'West Texas', False)

texas = Country('Texas', 0, 'republic')
tex_start_provs = {dal, hou, san, wte}
texas.add_cores(tex_start_provs)
texas.add_provinces(tex_start_provs)

# STATES WEST OF MISSISSIPPI
ark = Province('ark', 'Arkansas', False)
ari = Province('ari', 'Arizona', True)
col = Province('col', 'Colorado', True)
dak = Province('dak', 'Dakotas', False)
haw = Province('haw', 'Hawaii', True)
ida = Province('ida', 'Idaho', False)
kan = Province('kan', 'Kansas', True)
lou = Province('lou', 'Louisiana', True)
mis = Province('mis', 'Missouri', True)
mta = Province('mta', 'Montana', False)
neb = Province('neb', 'Nebraska', False)
nev = Province('nev', 'Nevada', False)
nme = Province('nme', 'New Mexico', False)
okl = Province('okl', 'Oklahoma', False)
ore = Province('ore', 'Oregon', True)
uta = Province('uta', 'Utah', False)
was = Province('was', 'Washington', True)
wyo = Province('wyo', 'Wyoming', False)

# CHICAGO
chi = Province('chi', 'Chicago', True)
ind = Province('ind', 'Indiana', False)
iow = Province('iow', 'Iowa', False)
mil = Province('mil', 'Milwaukee', True)
min = Province('min', 'Minneapolis', True)

chicago = Country('Chicago', 0, 'republic')
chi_start_provs = {chi, ind, iow, mil, min}
chicago.add_cores(chi_start_provs)
chicago.add_provinces(chi_start_provs)

# FLORIDA
fpa = Province('fpa', 'Florida Panhandle', False)
jac = Province('jac', 'Jacksonville', True)
mia = Province('mia', 'Miami', True)
tam = Province('tam', 'Tampa', True)

florida = Country('Florida', 0, 'republic')
flo_start_provs = {fpa, jac, mia, tam}
florida.add_cores(flo_start_provs)
florida.add_provinces(flo_start_provs)

# NEW YORK
nje = Province('nje', 'New Jersey', True)
nyc = Province('nyc', 'New York City', True)
nys = Province('nys', 'New York State', False)
phi = Province('phi', 'Philadelphia', True)
wpe = Province('wpe', 'West Pennsylvania', False)

new_york = Country('New York', 0, 'republic')
ny_start_provs = {nje, nyc, nys, phi, wpe}
new_york.add_cores(ny_start_provs)
new_york.add_provinces(ny_start_provs)

# STATES EAST OF MISSISSIPPI
dso = Province('dso', 'Deep South', False)
geo = Province('geo', 'Georgia', True)
ken = Province('ken', 'Kentucky', False)
mai = Province('mai', 'Maine', False)
mas = Province('mas', 'Massachusetts', True)
mic = Province('mic', 'Michigan', True)
nca = Province('nca', 'North Carolina', True)
ohi = Province('ohi', 'Ohio', True)
sca = Province('sca', 'South Carolina', False)
ten = Province('ten', 'Tennessee', True)
upe = Province('upe', 'Upper Peninsula', False)
vem = Province('vem', 'Vermont', False)
vir = Province('vir', 'Virginia', False)
wdc = Province('wdc', 'Washington DC', True)
wvi = Province('wvi', 'West Virginia', False)

# MEXICO
gua = Province('gua', 'Guadalajara', True)
gue = Province('gue', 'Guerrero', False)
mex = Province('mex', 'Mexico', True)
oax = Province('oax', 'Oaxaca', False)
pot = Province('pot', 'Potosi', False)
ver = Province('ver', 'Veracruz', True)

mexico = Country('Mexico', 0, 'republic')
mex_start_provs = {gua, gue, mex, oax, pot, ver}
mexico.add_cores(mex_start_provs)
mexico.add_provinces(mex_start_provs)

# REST OF MEXICO
baj = Province('baj', 'Baja California', False)
chh = Province('chh', 'Chihuahua', True)
chp = Province('chp', 'Chiapas', False)
coa = Province('coa', 'Coahulia', False)
dur = Province('dur', 'Durango', True)
nle = Province('nle', 'Nuevo Leon', True)
tab = Province('tab', 'Tabasco', False)
yuc = Province('yuc', 'Yucatan', True)

# CUBA
cam = Province('cam', 'Camaguey', False)
hav = Province('hav', 'Havana', True)
hol = Province('hol', 'Holguin', True)
kin = Province('kin', 'Kingston', True)

cuba = Country('Cuba', 0, 'republic')
cub_start_provs = {cam, hav, hol, kin}
cuba.add_cores(cub_start_provs)
cuba.add_provinces(cub_start_provs)

# PERU
ant = Province('ant', 'Antioquia', False)
bog = Province('bog', 'Bogota', True)
cal = Province('cal', 'Cali', True)
ecu = Province('ecu', 'Ecuador', False)
guj = Province('guj', 'Guajira', False)
lim = Province('lim', 'Lima', True)
vic = Province('vic', 'Vichada', False)

peru = Country('Peru', 0, 'republic')
per_start_provs = {ant, bog, cal, ecu, guj, lim, vic}
peru.add_cores(per_start_provs)
peru.add_provinces(per_start_provs)

# REST OF AMERICAS
cri = Province('cri', 'Costa Rica', False)
dom = Province('dom', 'Dominician Republic', True)
els = Province('els', 'El Salvador', False)
gut = Province('gut', 'Guatemala', True)
hai = Province('hai', 'Haiti', False)
hon = Province('hon', 'Honduras', False)
nic = Province('nic', 'Nicaragua', True)
pan = Province('pan', 'Panama', True)
ven = Province('ven', 'Venezuela', True)
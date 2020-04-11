from states import Province, Country, SeaZone, Person

#               PROVINCES & COUNTRIES INITIALISATION

# BRITISH COLUMBIA
anc = Province('anc', 'Anchorage', True)
cgy = Province('cgy', 'Calgary', True)
nbc = Province('nbc', 'Northern British-Columbia', False)
van = Province('van', 'Vancouver', True)
yuk = Province('yuk', 'Yukon', False)

british_columbia = Country('British Columbia', 'British Columbian', 0, 'republic')
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

quebec = Country('Quebec', 'Quebec', 0, 'republic')
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

california = Country('California', 'Californian', 0, 'republic')
cal_start_provs = {los, sdi, sfi}
california.add_cores(cal_start_provs)
california.add_provinces(cal_start_provs)


# TEXAS
dal = Province('dal', 'Dallas', True)
hou = Province('hou', 'Houston', True)
san = Province('san', 'San Antonio', True)
wte = Province('wte', 'West Texas', False)

texas = Country('Texas', 'Texan', 0, 'republic')
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

chicago = Country('Chicago', 'Chicagoan', 0, 'republic')
chi_start_provs = {chi, ind, iow, mil, min}
chicago.add_cores(chi_start_provs)
chicago.add_provinces(chi_start_provs)

# FLORIDA
fpa = Province('fpa', 'Florida Panhandle', False)
jac = Province('jac', 'Jacksonville', True)
mia = Province('mia', 'Miami', True)
tam = Province('tam', 'Tampa', True)

florida = Country('Florida', 'Floridian', 0, 'republic')
flo_start_provs = {fpa, jac, mia, tam}
florida.add_cores(flo_start_provs)
florida.add_provinces(flo_start_provs)

# NEW YORK
nje = Province('nje', 'New Jersey', True)
nyc = Province('nyc', 'New York City', True)
nys = Province('nys', 'New York State', False)
phi = Province('phi', 'Philadelphia', True)
wpe = Province('wpe', 'West Pennsylvania', False)

new_york = Country('New York', 'New Yorker', 0, 'republic')
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

mexico = Country('Mexico', 'Mexican', 0, 'republic')
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

cuba = Country('Cuba', 'Cuban', 0, 'republic')
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

peru = Country('Peru', 'Peruvian', 0, 'republic')
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

#               SEAZONES INITIALISATION

# ARCTIC
ARO = SeaZone('ARO', 'Arctic Ocean')
BAB = SeaZone('BAB', 'Baffin Bay')
BEF = SeaZone('BEF', 'Beaufort Sea')
BER = SeaZone('BER', 'Bering Sea')
GSL = SeaZone('GSL', 'Gulf of St-Lawrence')
HUB = SeaZone('HUB', 'Hudson Bay')
NAO = SeaZone('NAO', 'North Atlantic Ocean')
SOL = SeaZone('SOL', 'Sea of Labrador')

# MID ATLANTIC
APB = SeaZone('APB', 'Apalachee Bay')
BET = SeaZone('BET', 'Bermuda Triangle')
CHB = SeaZone('CHB', 'Chesapeake Bay')
ECO = SeaZone('ECO', 'East Coast')
MAB = SeaZone('MAB', 'Massachusetts Bay')
MAO = SeaZone('MAO', 'Mid Atlantic Ocean')
MAY = SeaZone('MAY', 'Cape May')
SOF = SeaZone('SOF', 'Sea of Florida')
SOS = SeaZone('SOS', 'Sea of Sargasso')

# SOUTH ATLANTIC
CAT = SeaZone('CAT', 'Cayman Trench')
ECS = SeaZone('ECS', 'East Caribbean')
GMO = SeaZone('GMO', 'Gulf of Mosquitos')
GOC = SeaZone('GOC', 'Gulf of Campeche')
GOH = SeaZone('GOH', 'Gulf of Hond')
GOM = SeaZone('GOM', 'Gulf of Mexico')
LES = SeaZone('LES', 'Lesser Antilles')
SCS = SeaZone('SCS', 'South Caribbean')
SOY = SeaZone('SOY', 'Straits of Yucatan')
WCS = SeaZone('WCS', 'West Caribbean')

# GREAT LAKES
LER = SeaZone('LER', 'Lake Erie')
LHU = SeaZone('LHU', 'Lake Huron')
LMI = SeaZone('LMI', 'Lake Michigan')
LON = SeaZone('LON', 'Lake Ontario')
LSU = SeaZone('LSU', 'Lake Superior')


# NORTH PACIFIC
GCA = SeaZone('GCA', 'Gulf of California')
GOA = SeaZone('GOA', 'Gulf of Alaska')
GSC = SeaZone('GSC', 'Gulf of Santa Catalina')
MPO = SeaZone('MPO', 'Mid Pacific Ocean')
NPO = SeaZone('NPO', 'North Pacific Ocean')
QCS = SeaZone('QCS', 'Queen Charlotte Sound')
SJF = SeaZone('SJF', 'Straits of Juan da Fuca')
WCO = SeaZone('WCO', 'West Coast')

# SOUTH PACIFIC
COB = SeaZone('COB', 'Coronado Bay')
COM = SeaZone('COM', 'Coast of Mexico')
GAL = SeaZone('GAL', 'Galapagos')
GOF = SeaZone('GOF', 'Gulf of Fonesca')
GOG = SeaZone('GOG', 'Gulf of Guayaquil')
GOP = SeaZone('GOP', 'Gulf of Panama')
GOT = SeaZone('GSC', 'Gulf of Tehuantepec')
SPO = SeaZone('SPO', 'South Pacific Ocean')
SWP = SeaZone('SWP', 'South West Pacific Ocean')

#               PROVINCES BORDERING

# BRITISH COLUMBIA
anc.set_bordering({ARO,BEF,BER,GOA,nbc,QCS,van,yuk})
cgy.set_bordering({mta,nbc,nwt,sas,van})
nbc.set_bordering({anc,cgy,nwt,van,yuk})
van.set_bordering({anc,cgy,ida,mta,nbc,QCS,SJF,was})
yuk.set_bordering({anc,BEF,nbc,nwt})

# QUEBEC
abi.set_bordering({HUB,mon,non,que,ung})
bea.set_bordering({gas,mai,mon,nys,ont,que,vem})
cot.set_bordering({GSL,lab,que,ung})
gas.set_bordering({bea,GSL,mai,nbr,que})
mon.set_bordering({abi,bea,non,ont,que})
que.set_bordering({abi,bea,cot,gas,GSL,mon,ung})
ung.set_bordering({abi,cot,HUB,lab,nun,que,SOL})

# REST OF CANADA + GREENLAND
gre.set_bordering({ARO,BAB,NAO,SOL})
lab.set_bordering({cot,GSL,SOL,ung})
man.set_bordering({dak,HUB,min,non,nun,sas,won})
nbr.set_bordering({gas,GSL,MAB,mai,nsc})
nfl.set_bordering({GSL,NAO,SOL})
non.set_bordering({abi,HUB,man,mon,ont,won})
nsc.set_bordering({GSL,MAB,NAO,nbr})
nun.set_bordering({BAB,BEF,HUB,man,nwt,sas,SOL,ung})
nwt.set_bordering({BEF,cgy,nbc,nun,sas,yuk})
ont.set_bordering({bea,LER,LHU,LON,LSU,mic,mon,non,nys,upe,won})
sas.set_bordering({cgy,dak,man,mta,nun,nwt})
won.set_bordering({LSU,man,min,non,ont})

# CALIFORNIA
los.set_bordering({GSC,nev,sdi,sfi,WCO})
sdi.set_bordering({ari,baj,GSC,los,nev})
sfi.set_bordering({los,nev,ore,WCO})

# TEXAS
dal.set_bordering({ark,hou,lou,nme,okl,san,wte})
hou.set_bordering({dal,GOM,lou,san})
san.set_bordering({coa,dal,GOM,hou,nle,wte})
wte.set_bordering({chh,coa,dal,nme,san})

# STATES WEST OF MISSISSIPPI
ark.set_bordering({dal,dso,kan,lou,mis,okl,ten})
ari.set_bordering({baj,chh,col,nev,nme,sdi,uta})
col.set_bordering({ari,kan,neb,nme,okl,uta,wyo})
dak.set_bordering({iow,man,min,mta,neb,sas,wyo})
haw.set_bordering({MPO,NPO,SPO,SWP})
ida.set_bordering({mta,nev,ore,uta,van,was,wyo})
kan.set_bordering({col,mis,neb,okl})
lou.set_bordering({APB,ark,dal,dso,GOM,hou})
mis.set_bordering({ark,chi,iow,kan,ken,neb,okl,ten})
mta.set_bordering({cgy,dak,ida,sas,van,wyo})
neb.set_bordering({col,dak,iow,kan,mis,wyo})
nev.set_bordering({ari,ida,los,ore,sdi,sfi,uta})
nme.set_bordering({ari,chh,col,dal,okl,wte})
okl.set_bordering({ark,col,dal,kan,mis,nme})
ore.set_bordering({ida,nev,sfi,SJF,was,WCO})
uta.set_bordering({ari,col,ida,nev,wyo})
was.set_bordering({ida,ore,SJF,van})
wyo.set_bordering({col,dak,ida,mta,neb,uta})

# CHICAGO
chi.set_bordering({ind,iow,ken,LMI,mil,mis})
ind.set_bordering({chi,ken,LMI,mic,ohi})
iow.set_bordering({chi,dak,mil,min,mis,neb})
mil.set_bordering({chi,iow,LMI,LSU,min,upe})
min.set_bordering({dak,iow,LSU,man,mil,won})

# FLORIDA
fpa.set_bordering({APB,dso,geo,jac,tam})
jac.set_bordering({ECO,fpa,geo,mia,tam})
mia.set_bordering({APB,ECO,jac,SOF,tam})
tam.set_bordering({APB,fpa,jac,mia})

# NEW YORK
nje.set_bordering({MAY,nyc,phi,wdc})
nyc.set_bordering({mas,MAY,nje,nys,phi})
nys.set_bordering({bea,LER,LON,mas,nyc,ont,phi,vem,wpe})
phi.set_bordering({nje,nyc,nys,wdc,wpe})
wpe.set_bordering({LER,nys,ohi,phi,wdc,wvi})

# STATES EAST OF MISSISSIPPI
dso.set_bordering({APB,ark,fpa,geo,lou,ten})
geo.set_bordering({dso,ECO,fpa,jac,nca,sca,ten})
ken.set_bordering({chi,ind,mis,ohi,ten,vir,wvi})
mai.set_bordering({bea,gas,MAB,nbr,vem})
mas.set_bordering({MAB,MAY,nyc,nys,vem})
mic.set_bordering({ind,LER,LHU,LMI,ohi,ont,upe})
nca.set_bordering({CHB,ECO,geo,sca,ten,vir})
ohi.set_bordering({ind,ken,LER,mic,wpe,wvi})
sca.set_bordering({ECO,geo,nca})
ten.set_bordering({ark,dso,geo,ken,mis,nca,vir})
upe.set_bordering({LHU,LMI,LSU,mic,mil,ont})
vem.set_bordering({bea,MAB,mai,mas,nys})
vir.set_bordering({CHB,ken,nca,ten,wdc,wvi})
wdc.set_bordering({CHB,MAY,nje,phi,vir,wpe,wvi})
wvi.set_bordering({ken,ohi,vir,wdc,wpe})

# MEXICO
gua.set_bordering({COM,dur,GCA,gue,mex,pot})
gue.set_bordering({COM,gua,mex,oax})
mex.set_bordering({gua,gue,oax,pot,ver})
oax.set_bordering({chp,COM,GOT,gue,mex,ver})
pot.set_bordering({coa,dur,GOC,gua,mex,nle,ver})
ver.set_bordering({chp,GOC,mex,oax,pot,tab})

# REST OF MEXICO
baj.set_bordering({ari,chh,GCA,GSC,MPO,NPO,sdi})
chh.set_bordering({ari,baj,coa,dur,GCA,nme,wte})
chp.set_bordering({GOT,gut,oax,tab,ver})
coa.set_bordering({chh,dur,nle,pot,san,wte})
dur.set_bordering({chh,coa,GCA,gua,pot})
nle.set_bordering({coa,GOC,GOM,pot,san})
tab.set_bordering({chp,GOC,gut,ver,yuc})
yuc.set_bordering({GOC,GOH,GOM,gut,SOY,tab})

# CUBA
cam.set_bordering({BET,CAT,hav,hol,SOF,WCS})
hav.set_bordering({cam,SOF,SOY,WCS})
hol.set_bordering({BET,cam,CAT})
kin.set_bordering({CAT,ECS,WCS})

# PERU
ant.set_bordering({bog,cal,guj,SCS,vic})
bog.set_bordering({ant,cal,ecu,lim,vic})
cal.set_bordering({ant,bog,ecu,GOG,GOP,pan,SCS})
ecu.set_bordering({bog,cal,GAL,GOG,lim})
guj.set_bordering({ant,SCS,ven,vic})
lim.set_bordering({bog,ecu,GAL,GOG})
vic.set_bordering({ant,bog,guj,ven})

# REST OF AMERICAS
cri.set_bordering({COB,GMO,nic,pan})
dom.set_bordering({BET,ECS,hai,LES,SOS})
els.set_bordering({COM,GOF,gut,hon})
gut.set_bordering({chp,COM,els,GOH,GOT,hon,tab,yuc})
hai.set_bordering({BET,CAT,dom,ECS})
hon.set_bordering({els,GOF,GOH,gut,nic,WCS})
nic.set_bordering({COB,cri,GMO,GOF,hon,WCS})
pan.set_bordering({cal,COB,cri,GMO,GOP,SCS})
ven.set_bordering({ECS,guj,LES,SCS,vic})

#               SEAZONES BORDERING

# ARCTIC
ARO.set_bordering({anc,BAB,BEF,BER,nun})
BAB.set_bordering({ARO,gre,nun,SOL})
BEF.set_bordering({anc,ARO,nun,nwt,yuk})
BER.set_bordering({anc,ARO,GOA})
GSL.set_bordering({cot,gas,lab,NAO,nbr,nfl,nsc,que,SOL})
HUB.set_bordering({abi,man,non,nun,SOL,ung})
NAO.set_bordering({gre,GSL,MAB,MAO,nfl,nsc,SOL})
SOL.set_bordering({BAB,gre,GSL,HUB,lab,NAO,nfl,nun,ung})

# MID ATLANTIC
APB.set_bordering({dso,fpa,GOM,lou,mia,SOF,tam})
BET.set_bordering({cam,CAT,dom,ECO,hai,hol,MAY,MAO,SOF,SOS})
CHB.set_bordering({ECO,MAY,nca,vir,wdc})
ECO.set_bordering({BET,CHB,geo,jac,MAY,mia,nca,sca,SOF})
MAB.set_bordering({mai,MAO,mas,MAY,NAO,nbr,nsc,vem})
MAO.set_bordering({BET,MAB,MAY,NAO,SOS})
MAY.set_bordering({BET,CHB,ECO,MAB,MAO,mas,nje,nyc,wdc})
SOF.set_bordering({APB,BET,cam,ECO,GOM,hav,mia,SOY})
SOS.set_bordering({BET,dom,LES,MAO})

# SOUTH ATLANTIC
CAT.set_bordering({BET,cam,ECS,hai,hol,kin,WCS})
ECS.set_bordering({CAT,dom,hai,kin,LES,SCS,ven,WCS})
GMO.set_bordering({cri,nic,pan,SCS,WCS})
GOC.set_bordering({GOM,nle,pot,tab,ver,yuc})
GOH.set_bordering({gut,hon,SOY,WCS,yuc})
GOM.set_bordering({APB,GOC,hou,lou,nle,san,SOF,SOY,yuc})
LES.set_bordering({dom,ECS,SOS,ven})
SCS.set_bordering({ant,cal,ECS,GMO,guj,pan,ven,WCS})
SOY.set_bordering({GOH,GOM,hav,SOF,WCS,yuc})
WCS.set_bordering({cam,CAT,ECS,GMO,GOH,hav,hon,kin,nic,SCS,SOY})

# GREAT LAKES
LER.set_bordering({}) # not yet implemented
LHU.set_bordering({}) # not yet implemented
LMI.set_bordering({chi,ind,LHU,mic,mil,upe})
LON.set_bordering({}) # not yet implemented
LSU.set_bordering({mil,min,ont,upe,won})


# NORTH PACIFIC
GCA.set_bordering({baj,chh,COM,dur,gua,MPO})
GOA.set_bordering({anc,BER,NPO,QCS,SJF,WCO})
GSC.set_bordering({baj,los,NPO,sdi,WCO})
MPO.set_bordering({baj,COM,GCA,haw,NPO,SPO})
NPO.set_bordering({baj,GOA,GSC,haw,MPO,SWP,WCO})
QCS.set_bordering({anc,GOA,SJF,van})
SJF.set_bordering({GOA,ore,QCS,van,was,WCO})
WCO.set_bordering({GOA,GSC,los,NPO,ore,sfi,SJF})

# SOUTH PACIFIC
COB.set_bordering({cri,GOF,GOG,GOP,nic,pan})
COM.set_bordering({els,GAL,GCA,GOF,GOT,gua,gue,gut,MPO,oax,SPO})
GAL.set_bordering({COM,GOF,GOG,lim,SPO})
GOF.set_bordering({COB,COM,els,GAL,GOG,hon,nic})
GOG.set_bordering({cal,COB,ecu,GAL,GOF,GOP,lim})
GOP.set_bordering({cal,COB,GOG,pan})
GOT.set_bordering({chp,COM,gut,oax})
SPO.set_bordering({COM,GAL,haw,MPO,SWP})
SWP.set_bordering({haw,NPO,SPO})

english_speaking = {british_columbia, california, texas, chicago, florida, new_york}
for country in english_speaking:
    country.set_languages({'en'})
mexico.set_languages({'es-mx'})
quebec.set_languages({'en','fr'})
cuba.set_languages({'es'})
peru.set_languages({'es'})

all_countries = {british_columbia, quebec, california, texas, chicago, florida, new_york, mexico, cuba, peru}
new_man = Person('Johnny', 'Cash')
for country in all_countries:
    country.set_ruler(new_man)
    country.set_capital('some city')
    country.set_official_name('official name example')

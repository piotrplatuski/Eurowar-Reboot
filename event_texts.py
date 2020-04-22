from events import *

# Events in which one country gets affected.

one1 = Event(1, "A comet has been sighted in <country1>. It's an omen!")
# -1 stability
one2 = Event(1, "<rulertype1> <ruler1> of <country1>, has had a heart attack. He passed away.")
# -1 stability, maybe not? could be RNG of either 0 and -1
one3 = Event(1, "A town in <province1> has suffered a fire of grand scale."
                " People have fled the town to other settlements of <country1>.")
# -economy points
one4 = Event(1, "The <countrian1> economy has received a hit due to the declaration of"
                " bancrupcy by one of the leading companies in <country1>.")
one5_1 = Event(1, "A ferocious storm has left thousands of <countrian1> people without a home."
                  "Devastating damage was inflicted by the storm.")
one5_2 = Event(1, "A moderate storm has left hundreds of <countrian1> people without a home."
                  "Serious damage was inflicted by the storm.")
one5_3 = Event(1, "A mild storm has left dozens of <countrian1> people without a home. "
                  "Sustainable damage was inflicted by the storm.")
# -economy points, could also have chance for stability hit depending on severity
one6 = Event(1, "Recently a minister of <country1> has made provoking remarks towards the"
                " general public. A demonstration was held in <cap1> by some furious"
                " citizens.")
one7 = Event(1, "The <countrian1> economy has received a significant boost because"
                " of the recent good decisions of local businessmen.")
one8 = Event(1, "The government building of <country1> has catched fire. The fire could"
                " finally be extinguished, but repairing the building shall be expensive."
                " The cause is yet unknown.")
one9 = Event(1, "An important government advisor, <man1>, has been murdered by an extremist"
                " from the opposition. The <countrian1> state is in turmoil.")
one10 = Event(1, "A <countrian1> minister has been caught on corruption. He has been convicted"
                 " and awaits trial.")
one11 = Event(1, "A recent scandal in <country1> involving one of the generals caused disapprovement"
                 " of the higher ranks in the army. Many soldiers are revolting against superiors.")
one12 = Event(1, "There was an assassination attempt in <country1>. <ruler1>'s bodyguards however"
                 " managed to prevent the aggressor from his deed.")
one13 = Event(1, "The <countrian1> ruler, <ruler1>, was killed by an assassin. The country is"
                 " mourning his death.")
one14 = Event(1, "A mysterious disease has broken out in <countrian1> province of <province1> and taken dozens of lives"
                 ". The disease has disappeared as suddenly as it appeared.")
# Not sure what the effects could be. Didn't want a pandemic of any sort since we don't have any of follow-up events.
one15 = Event(1, "In <country1>, there have recently been problems regarding the distribution"
                 " of food to the remote areas. The people expect the government to act.")
one16 = Event(1, "A <countrian1> passenger train has derailed in <province1>."
                 "There are dozens of casualties and hundreds of wounded passengers.")
one17 = Event(1, "Last season's exceptionally good harvest has proved a boost to the <countrian1>"
                 " economy.")
one18 = Event(1, "Last season's exceptionally bad harvest has proved an issue to the <countrian1>"
                 " economy.")
one19 = Event(1, "Farmers of <country1> are protesting against the government. They demand"
                 " more subsidies from the state.")
one20 = Event(1, "There was a strike of police forces in <country1>. They demand higher wages.")
one21 = Event(1, "Two <countrian1> passenger trains have collided to each other in <province1>. "
                 "There are hundreds of causalties and wounded passengers.")
one22 = Event(1, "A <countrian1> cargo train has derailed in <supplycenter1>. The crew has died, but the tons of cargo "
                 "that was lost in the derailment will be recovered in next weeks.")
# Income from <supplycenter1> will be delayed to next year
one23_1 = Event(1, "A plentiful oil reserve has been found in <province1>. The reserve will not only boost <country1>'s"
                   " economy, but also bring stability.") # Player version
one23_2 = Event(1, "A plentiful oil reserve has been found in <province1>. Both the reserve and the province will"
                   "surely become a rewarding target to surrounding countries.") # Neutral version
# +stability, maybe even... upgrade of province. Maybe it would HAVE to be a non-SC, but in such case "trigger" condit-
# ion would be that every country would already own a non-SC province, otherwise California will not be able to receive
# it. It could also have a chance to happen in neutral non-SC province which has no "investments" from any country.
one23_3 = Event(1, "A plentiful oil reserve has been found in Nevada. Both the reserve and the province will surely "
                   "become a rewarding target to <country1> .")
# Californian workaround version before it gets a non-SC - > OnlyCalifornia, if they take over it, gets +1 stability
one24 = Event(1, "Fascists, led by <name1>, have organized a massive rally from <province1> to <capital1>. ")
"As they passed through villages and towns their numbers have progresively increased."
" They are now very close to the capital city. [Choices:]"
# How to implement for example: <country1>['stability'] -= 1?
# Also, introduce rank of importance to events.

# Events in which two countries get affected.

two1 = Event(2, "The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                " seemed to understand eachother well and wish to cooperate where possible.")
two2 = Event(2, "There was a conflict on the border between <country1> and <country2bordering1>. It started with"
                " two antagonizing peasants and broadened to the scope of whole villages.")
two3 = Event(2, "A <countrian1> politician has insulted <ruler2>, the <countrian2> ruler, and disapproved his"
                " recent policies.")
two4 = Event(2, "There was a terrorist attack in <country1>. The assassin is a <countrian2> man called"
                " <man2>. Several innocent citizens died. The criminal got shot by police officers.")
two5 = Event(2, "A small <countrian1> airplane has crashed while crossing <countrian2> territory. Few passengers"
                " died on the spot, one miraculously survived.")
two6 = Event(2, "A <countrian1> automobile company is making huge profits from export to <country2>.")
two7 = Event(2, "There seems to be much interest in <country1> for the culture and language of <country2> lately."
                " Cinemas in <cap1> display movies of <countrian2> production regularly nowadays.")
two8 = Event(2, "The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                " didn't go along very well and the whole meeting felt forced and out of place.")
two9 = Event(2, "A dangerous storm has passed over <country1> and <country2bordering1>. There are dozens of"
                " casualties in both countries.")
two10 = Event(2, "A small <countrian1> airplane has crashed while crossing <countrian2> territory. The few"
                 " passengers were unfortunately all killed on the spot.")

# MONARCHY

mon1 = Event(1, "Heir to the throne has been assassinated as he was being driven around <cap1>. "
                "The assassin was identified as <name1> who had previously expressed anti-monarchist remarks. "
                "He might have been helped by someone close to the royal family.")
# I think it's fair for -1 stability hit

mon2 = Event(1, "Working class protesters of <country1>, led by promises of equality and better future for the working "
                "class, have stormed and taken over the royal palace. The royal family was murdered in cold blood. "
                "Only <ruler1> was spared of this fate as he was outside <capital1> during this event.")
# Three choices: Switch to Republic (abdication of ruler) and -1 stability hit, switch to Communism (the ruler is
# eventually found and killed), or -2 stability hit because no heir.
mon3 = Event(1, "Fascists, led by <name1>, have organized a massive rally from <province1> to <capital1>."
                " As they passed through villages and towns their numbers have progresively increased."
                " They are now very close to the capital city.")
# Choices: Declare a state of siege (can't have any movement to or from capital province, lose all income in capital
# for this year), Switch to Fascism (king hands power to the fascist leader, however king stays as king).
####################################################################################################
# EVENTS BASED ON GOVERNMENT
# Fascism
G_fas1 = Event(1, "<ruler1> Youth, the official <country1>'s youth organization, has noticed a spike of new enlistees the last year.")
# Monarchy
G_mon1 = Event(1, "Important nobles from all over Americas have come to <capital1>, where influential <countrian1> noble, <man1>, has "
	          "thrown a ball party. It even had retrievers!")
# Republic
G_rep1 = Event(1, "A fight has broken out in <countrian1> Parliament when the governing party and the opposition started antagonizing "
	          "each other. The opposition was rushed to hospitals.")
G_rep2 = Event(1, "The last <countrian1> general election has noticed a spike of voters, however, the current governing party has "
	          "retained the majority.")
G_rep3 = Event(1, "The <countrian1> suffragettes have held a rally in <capital1> where they demanded the right to vote for women in "
	          "<country1>.")
####################################################################################################
# VERY POSITIVE EVENTS
VP_com1 = Event(1, "The communism has brought long-sought equality to <countrian1> people. Proletariat is finally united, produce is "
                   "plentiful... and propaganda is more intricate than ever before.")
VP_fas1 = Event(1, "The government in <country1> works like a well-oiled machine. Dissidents are effectively suppressed, economy is "
                   "blooming and people are very supportive of the fascist rule.")
VP_mon1 = Event(1, "<ruler1> is well-beloved monarch in <country1>. Under Hisrule both nobles and commoners are content, military is "
                   "ready to fight for their <rulertype1>, while the Cabinet of Ministers is ready to ensure <rulertype1>'s will.")
VP_rep1 = Event(1, "Citizens of <country1> are proud of their rights grantedby amendments in the constitution, while the <countrian1> "
                   "institutions are an example to the rest of world.")
####################################################################################################
# DISASTERS
D_comet = Event(1, "A comet has been sighted in <country1>. It's an omen!")

D_nrd1 = Event(1, "<rulertype1> <ruler1> of <country1> has had a heart attack and passed away. The nation is celebrating the great "
                  "news.")
D_nrd2 = Event(1, "<rulertype1> <ruler1> of <country1> has had a heart attack and passed away. The nation is mourning their late "
                  "<rulertype1>.")
D_nrd3 = Event(1, "<rulertype1> <ruler1> of <country1> has had a heart attack. The <rulertype1> is dead, long live the <rulertype1>!")

D_sto1 = Event(1, "A ferocious storm has left thousands of <countrian1> people without a home. Devastating damage was inflicted by the "
                  "storm.")
D_sto2 = Event(1, "A moderate storm has left hundreds of <countrian1> people without a home. Serious damage was inflicted by the "
                  "storm.")		
D_sto3 = Event(1, "A mild storm has left dozens of <countrian1> people without a home. Sustainable damage was inflicted by the storm.")
	
D_tra1 = Event(1, "A <countrian1> passenger train has derailed in <province1>. There are dozens of causalties and hundreds of wounded "
                  "passengers.")
D_tra2 = Event(1, "Two <countrian1> passenger trains have collided to each other in <province1>. There are hundreds of causalties and "
                  "wounded passengers.")
# D_tra3 - [Income from <supplycenter1> will be delayed to next year.]
D_tra3 = Event(1, "A <countrian1> cargo train has derailed in <supplycenter1>. The crew has died, but the tons of cargo that was lost "
                  "in the derailment will be recovered in next weeks.")
####################################################################################################
# FORTUNES 
F_gol1 = Event(1, "<countrian1> cartographers have accidentally found a gold vein in <province1> while marking the area. It looks "
                  "promising to investigate further.")

F_oil1 = Event(1, "A plentiful oil reserve has been found in <province1>. The reserve will not only boost <country1>'s economy, but "
                  "also bring stability.")

F_har1 = Event(1, "Last season's exceptionally good harvest has filled the <countrian1> granaries to the brim. It will provide much "
                  "needed stability to <country1>.")
F_har2 = Event(1, "Last season's exceptionally good harvest has filled the <countrian1> granaries to the brim. It will provide "
                  "<country1> with opportunities to trade.")
####################################################################################################
# POLITICS
P_pro1 = Event(1, "<man1>, a minister of <country1>, has made provoking remarks towards the general public. A demonstration was held "
	         "in <capital1> by some furious citizens.")

P_kni1 = Event(1, "A minister of <country1>, <man1>, was attacked by a man armed with a knife. Fortunately the minister was carrying "
	          "a revolver and killed the attacker.")
# I think high stability in such cases should be 6 and more than 6 as that number is high enough. Low stability 5 or below.
# High stability Republic & Monarchy version (low stab is kni1):
P_kni2 = Event(1, "A minister of <country1>, <man1>, was attacked by a man armed with a knife. Fortunately for the minister, a "
	          "passerby, who was carrying a revolver, heard the commotion. He came and killed the attacker.")
# High stability Fascism (low stab is kni1):
P_kni3 = Event(1, "A minister of <country1>, <man1>, was attacked by a man armed with a knife. Fortunately for the minister, an"
		  "officer, who was carrying a revolver, heard the commotion. He came and killed the attacker.")
# Low stability Communism (high stab is kni1):
P_kni4 = Event(1, "A minister of <country1>, <man1>, was attacked by a man armed with a knife. Unortunately for the minister, a "
	          "passerby, who was also carrying a knife, heard the commotion. He came and they both killed the minister.")

P_ins1 = Event(2, "A <countrian1> politician has insulted <countrian2> <rulertype2> <ruler2>, and disapproved of his recent policies.")

P_for1 = Event(2, "The foreign ministers of <country1> and <country2> have met in <capital1>. They seemed to understand each other "
	          "well and wish to cooperate where it is possible.")
P_for2 = Event(2, "The foreign ministers of <country1> and <country2> have met in <capital1>. They didn't go along very well and the "
	          "whole meeting felt forced and out of place.")
####################################################################################################
#  MILITARY
M_cou1 = Event(1, "A troop of <countrian1> military forces attempted to overthrow <rulertype1> <ruler1>, but the <rulertype1>'s "
		  "guardsmen have stopped them. Interrogations revealed Gen. <surname1> as the author of the coup.")
# Monarchy version:
M_cou2 = Event(1, "A troop of <countrian1> military forces attempted to overthrow <rulertype1> <ruler1>, but the Royal Guard has "
	          "stopped them. Interrogations revealed Gen. <surname1> as the author of the coup.")
####################################################################################################
# NEUTRALS
N_gol1 = Event(0, "Local cartographers have accidentally found a gold vein in <province0> while marking the area. It looks promising "
                  "to investigate further.")

N_oil1 = Event(0, "A plentiful oil reserve has been found in <province0>. Both the reserve and the province will surely become a "
                  "rewarding target to surrounding countries.")
# uni stands for "unique", for specific provinces.
N_uni1 = Event(0, "After break up of the Union the state of Utah was never the same. After numerous sessions the Utahn government, "
                  "with titanic Mormon influence, reforms it to Deseret - a Mormon-run theocratic state.")
####################################################################################################

all = [one1, one2, one3, one4, one5_1, one5_2, one5_3, one6, one7, one8, one9]
for event in all:
    event.set_probability(1)
    event.set_effects('{country1} economy +400, stability -3, '
                      '{ruler1} fname Andrzej, lname Poniatowski')
all_probs = [event.get_probability() for event in all]

from events import *
####################################################################################################
# MONARCHY - UNIQUE
MU_ass = Event(1, "Heir to the throne has been assassinated as he was being driven around <capital1>. The assassin was identified as "
	          "<name1> who had previously expressed anti-monarchist remarks. Rumor has it that he was helped by someone close to "
	          "the royal family.")
MU_com = Event(1, "Working class protesters of <country1>, led by promises of equality and better future for the working class, have "
	          "stormed and taken over the royal palace. The royal family was murdered in cold blood. Only <ruler1> was spared of "
	          "this fate as he was outside <capital1> during this event.")
MU_fas = Event(1, "Fascists, led by <name1>, have organized a massive rally from <province1> to <capital1>. As they passed through "
	          "villages and towns their numbers have progresively increased. They are now very close to the capital city."
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
# ECONOMY
E_boo1 = Event(1, "The <countrian1> economy has been experiencing a significant boost lately as the exports to other countries grow.")
####################################################################################################
# MILITARY
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
N_uni2 = Event(0, "A Kansas man has been proposing to split Kansas state into two states - Kansas and Kansas City states. It has "
	          "garnered a lot of support, however, it wasn't enough to be considered by Kansas Government.")
N_uni3 = Event(0, "The Imperial Japanese Navy, under pretext of protecting huge local Japanese population, has invaded and taken over "
	          "Hawaii. While Hawaii won't be incorporated to the Japanese Empire fully just yet, it already was granted "
	          "administrative level of a prefecture.")

N_mis1 = Event(0, "The creator of knock knock joke has won a Nobel prize.")
####################################################################################################

all = [one1, one2, one3, one4, one5_1, one5_2, one5_3, one6, one7, one8, one9]
for event in all:
    event.set_probability(1)
    event.set_effects('{country1} economy +400, stability -3, '
                      '{ruler1} fname Andrzej, lname Poniatowski')
all_probs = [event.get_probability() for event in all]

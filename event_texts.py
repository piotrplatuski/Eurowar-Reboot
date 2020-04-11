# Events in which one country gets affected.
from events import *

ev1_1 = Event("A comet has been sighted in <country1>. It's an omen!", 1)
## -1 stability
ev1_2 = Event("<rulertype1> <ruler1> of <country1>, has had a heart attack. He passed away.", 1)
## -1 stability, maybe not? could be RNG of either 0 and -1
ev1_3 = Event("A town in <province1> has suffered a fire of grand scale."
              " People have fled the town to other settlements of <country1>.", 1)
## -economy points
ev1_4 = Event("The <countrian1> economy has received a hit due to the declaration of"
                     " bancrupcy by one of the leading companies in <country1>.", 1)
ev1_5_1 = Event("A ferocious storm has left thousands of <countrian1> people without a home."
                "Devastating damage was inflicted by the storm.", 1)
ev1_5_2 = Event("A moderate storm has left hundreds of <countrian1> people without a home."
                "Serious damage was inflicted by the storm.", 1)
ev1_5_3 = Event("A mild storm has left dozens of <countrian1> people without a home. "
                "Sustainable damage was inflicted by the storm.", 1)
## -economy points, could also have chance for stability hit depending on severity
ev1_6 = Event("Recently a minister of <country1> has made provoking remarks towards the"
                     " general public. A demonstration was held in <cap1> by some furious"
                     " citizens.", 1)
ev1_7 = Event("The <countrian1> economy has received a significant boost because"
                  " of the recent good decisions of local businessmen.", 1)
ev1_8 = Event("The government building of <country1> has catched fire. The fire could"
                     " finally be extinguished, but repairing the building shall be expensive."
                     " The cause is yet unknown.", 1)
ev1_9 = Event("An important government advisor, <man1>, has been murdered by an extremist"
                  " from the opposition. The <countrian1> state is in turmoil.", 1)
ev1_10 = Event("A <countrian1> minister has been caught on corruption. He has been convicted"
                   " and awaits trial.", 1)
ev1_11 = Event("A recent scandal in <country1> involving one of the generals caused disapprovement"
                   " of the higher ranks in the army. Many soldiers are revolting against superiors.", 1)
ev1_12 = Event("There was an assassination attempt in <country1>. <ruler1>'s bodyguards however"
                   " managed to prevent the aggressor from his deed.", 1)
ev1_13 = Event("The <countrian1> ruler, <ruler1>, was killed by an assassin. The country is"
                   " mourning his death.", 1)
ev1_14 = Event("A mysterious disease has broken out in <countrian1> province of <province1> and taken dozens of lives."
               " The disease has disappeared as suddenly as it appeared.", 1)
## Not sure what the effects could be. Didn't want a pandemic of any sort since we don't have any of follow-up events.
ev1_15 = Event("In <country1>, there have recently been problems regarding the distribution"
                   " of food to the remote areas. The people expect the government to act.", 1)
ev1_16 = Event("A <countrian1> train has derailed. There are many dead and wounded.", 1)
ev1_17 = Event("Last season's exceptionally good harvest has proved a boost to the <countrian1>"
                   " economy.", 1)
ev1_18 = Event("Last season's exceptionally bad harvest has proved an issue to the <countrian1>"
                   " economy.", 1)
ev1_19 = Event("Farmers of <country1> are protesting against the government. They demand"
                   " more subsidies from the state.", 1)
ev1_20 = Event("There was a strike of police forces in <country1>. They demand higher wages.", 1)

# How to implement for example: <country1>['stability'] -= 1?
# Also, introduce rank of importance to events.

# Events in which two countries get affected.

ev2_1 = Event("The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                  " seemed to understand eachother well and wish to cooperate where possible.", 2)
ev2_2 = Event("There was a conflict on the border between <country1> and <country2bordering1>. It started with"
                  " two antagonizing peasants and broadened to the scope of whole villages.", 2)
ev2_3 = Event("A <countrian1> politician has insulted <ruler2>, the <countrian2> ruler, and disapproved his"
                  " recent policies.", 2)
ev2_4 = Event("There was a terrorist attack in <country1>. The assassin is a <countrian2> man called"
                  " <man2>. Several innocent citizens died. The criminal got shot by police officers.", 2)
ev2_5 = Event("A small <countrian1> airplane has crashed while crossing <countrian2> territory. Few passengers"
                  " died on the spot, one miraculously survived.", 2)
ev2_6 = Event("A <countrian1> automobile company is making huge profits from export to <country2>.", 2)
ev2_7 = Event("There seems to be much interest in <country1> for the culture and language of <country2> lately."
                  " Cinemas in <cap1> display movies of <countrian2> production regularly nowadays.", 2)
ev2_8 = Event("The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                  " didn't go along very well and the whole meeting felt forced and out of place.", 2)
ev2_9 = Event("A dangerous storm has passed over <country1> and <country2bordering1>. There are dozens of"
                  " casualties in both countries.", 2)
ev2_10 = Event("A small <countrian1> airplane has crashed while crossing <countrian2> territory. The few"
                      " passengers were unfortunately all killed on the spot.", 2)

# MONARCHY

ev_mon1 = Event("Heir to the throne has been assassinated as he was being driven around <cap1>. "
                   "The assassin was identified as <name1> who had previously expressed anti-monarchist remarks. "
                   "He might have been helped by someone close to the royal family.", 1)
## I think it's fair for -1 stability hit

ev_mon2 = Event("Working class protesters of <country1>, led by promises of equality and better future for the working class, "
                   "have stormed and taken over the royal palace. The royal family was murdered in cold blood. Only <ruler1>"
                   " was spared of this fate as he was outside <capital1> during this event.", 1)
## Three choices: Switch to Republic (abdication of ruler) and -1 stability hit, switch to Communism (the ruler is eventually found and killed), or -2 stability hit because no heir.
ev_mon3 = Event("Fascists, led by <name1>, have organized a massive rally from <province1> to <capital1>."
                   " As they passed through villages and towns their numbers have progresively increased."
                   " They are now very close to the capital city.", 1)
## Choices: Declare a state of siege (can't have any movement to or from capital province, lose all income in capital for this year), Switch to Fascism (king hands power to the fascist leader, however king stays as king).

# VERY POSITIVE EVENTS (8 or more stability, low chance)

# Communism
# Fascism
ev_fas_pos1 = Event("The government in <country1> works like a well-oiled machine."
                       " Dissidents are effectively suppressed, economy is blooming and"
                       " people are very supportive of the fascist rule.", 1)
# Monarchy
ev_mon_pos1 = Event("<ruler1> is well-beloved monarch in <country1>. Under His rule both nobles and commoners are"
                    " content, military is ready to fight for their King, while the Cabinet of Ministers is"
                    " ready to ensure King's will.", 1)
# Republic

## +1 stability, +some economy points (amount could be RNG)

all = [ev1_1, ev1_2, ev1_3, ev1_4]
all_probs = [event.get_probability() for event in all]

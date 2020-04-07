# Events in which one country gets affected.
from events import *

event1_1 = Event("A comet has been sighted in <country1>. It's an omen!", 1)
event1_2 = Event("The ruler of <country1>, <ruler1>, has had a heart attack. He passed away.", 1)
event1_3 = Event("In <cap1>, there was a huge fire. The <countrian1> people are shocked.", 1)
event1_4 = Event("The <countrian1> economy has received a hit due to the declaration of"
                     " bancrupcy by one of the leading companies in <country1>.", 1)
event1_5 = Event("A dangerous storm has left many <countrian1> people without a home. Much"
                     " damage was done.", 1)
event1_6 = Event("Recently a minister of <country1> has made provoking remarks towards the"
                     " general public. A demonstration was held in <cap1> by some furious"
                     " citizens.", 1)
event1_7 = Event("The <countrian1> economy has received a significant boost because"
                     " of the recent good decisions of local businessmen.", 1)
event1_8 = Event("The government building of <country1> has catched fire. The fire could"
                     " finally be extinguished, but repairing the building shall be expensive."
                     " The cause is yet unknown.", 1)
event1_9 = Event("An important government advisor, <man1>, has been murdered by an extremist"
                     " from the opposition. The <countrian1> state is in turmoil.", 1)
event1_10 = Event("A <countrian1> minister has been caught on corruption. He has been convicted"
                      " and awaits trial.", 1)
event1_11 = Event("A recent scandal in <country1> involving one of the generals caused disapprovement"
                      " of the higher ranks in the army. Many soldiers are revolting against superiors.", 1)
event1_12 = Event("There was an assassination attempt in <country1>. <ruler1>'s bodyguards however"
                      " managed to prevent the aggressor from his deed.", 1)
event1_13 = Event("The <countrian1> ruler, <ruler1>, was killed by an assassin. The country is"
                      " mourning his death.", 1)
event1_14 = Event("A strange infectious disease has broken out in <cap1>. Some citizens are"
                      " fleeing the city. There are already several dead.", 1)
event1_15 = Event("In <country1>, there have recently been problems regarding the distribution"
                      " of food to the remote areas. The people expect the government to act.", 1)
event1_16 = Event("A <countrian1> train has derailed. There are many dead and wounded.", 1)
event1_17 = Event("Last season's exceptionally good harvest has proved a boost to the <countrian1>"
                      " economy.", 1)
event1_18 = Event("Last season's exceptionally bad harvest has proved an issue to the <countrian1>"
                      " economy.", 1)
event1_19 = Event("Farmers of <country1> are protesting against the government. They demand"
                      " more subsidies from the state.", 1)
event1_20 = Event("There was a strike of police forces in <country1>. They demand higher wages.", 1)

# How to implement for example: <country1>['stability'] -= 1?
# Also, introduce rank of importance to events.

# Events in which two countries get affected.

event2_1 = Event("The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                     " seemed to understand eachother well and wish to cooperate where possible.", 2)
event2_2 = Event("There was a conflict on the border between <country1> and <country2bordering1>. It started with"
                     " two antagonizing peasants and broadened to the scope of whole villages.", 2)
event2_3 = Event("A <countrian1> politician has insulted <ruler2>, the <countrian2> ruler, and disapproved his"
                     " recent policies.", 2)
event2_4 = Event("There was a terrorist attack in <country1>. The assassin is a <countrian2> man called"
                     " <man2>. Several innocent citizens died. The criminal got shot by police officers.", 2)
event2_5 = Event("A small <countrian1> airplane has crashed while crossing <countrian2> territory. Few passengers"
                     " died on the spot, one miraculously survived.", 2)
event2_6 = Event("A <countrian1> automobile company is making huge profits from export to <country2>.", 2)
event2_7 = Event("There seems to be much interest in <country1> for the culture and language of <country2> lately."
                     " Cinemas in <cap1> display movies of <countrian2> production regularly nowadays.", 2)
event2_8 = Event("The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                     " didn't go along very well and the whole meeting felt forced and out of place.", 2)
event2_9 = Event("A dangerous storm has passed over <country1> and <country2bordering1>. There are dozens of"
                     " casualties in both countries.", 2)
event2_10 = Event("A small <countrian1> airplane has crashed while crossing <countrian2> territory. The few"
                      " passengers were unfortunately all killed on the spot.", 2)

# ______________________________________________________________________________________________________________________
events1 = (event1_1, event1_2, event1_3, event1_4, event1_5, event1_6, event1_7, event1_8, event1_9, event1_10,
           event1_11, event1_12, event1_13, event1_14, event1_15, event1_16, event1_17, event1_18, event1_19, event1_20,
           )
events2 = (event2_1, event2_2, event2_3, event2_4, event2_5, event2_6, event2_7, event2_8, event2_9, event2_10,)

events1_prob = [event['prob'] for event in events1]
events2_prob = [event['prob'] for event in events2]

all_events = [events1, events2]
all_probs = [events1_prob, events2_prob]


def normalize_probs(target):
    """Multiplies probabilities to make the sum of the list equal to 1."""
    for lis in target:
        tot = sum(lis)
        if tot != 1:
            for number in range(len(lis)):
                lis[number] *= 1 / tot
    return target


normalize_probs(all_probs)

# Events in which one country gets affected.

event1_1 = dict(text="A comet has been sighted in <country1>. It's an omen!",
                prob=0.02, )
event1_2 = dict(text="The ruler of <country1>, <ruler1>, has had a heart attack. He passed away.",
                prob=0.02, )
event1_3 = dict(text="In <cap1>, there was a huge fire. The <countrian1> people are shocked.",
                prob=0.02)
event1_4 = dict(text="The <countrian1> economy has received a hit due to the declaration of"
                     " bancrupcy by one of the leading companies in <country1>.",
                prob=0.02)
event1_5 = dict(text="A dangerous storm has left many <countrian1> people without a home. Much"
                     " damage was done.",
                prob=0.02)
event1_6 = dict(text="Recently a minister of <country1> has made provoking remarks towards the"
                     " general public. A demonstration was held in <cap1> by some furious"
                     " citizens.",
                prob=0.02)
event1_7 = dict(text="The <countrian1> economy has received a significant boost because"
                     " of the recent good decisions of local businessmen.",
                prob=0.02)
event1_8 = dict(text="The government building of <country1> has catched fire. The fire could"
                     " finally be extinguished, but repairing the building shall be expensive."
                     " The cause is yet unknown.",
                prob=0.02)
event1_9 = dict(text="An important government advisor, <man1>, has been murdered by an extremist"
                     " from the opposition. The <countrian1> state is in turmoil.",
                prob=0.02)
event1_10 = dict(text="A <countrian1> minister has been caught on corruption. He has been convicted"
                      " and awaits trial.",
                 prob=0.02)
event1_11 = dict(text="A recent scandal in <country1> involving one of the generals caused disapprovement"
                      " of the higher ranks in the army. Many soldiers are revolting against superiors.",
                 prob=0.02)
event1_12 = dict(text="There was an assassination attempt in <country1>. <ruler1>'s bodyguards however"
                      " managed to prevent the aggressor from his deed.",
                 prob=0.02)
event1_13 = dict(text="The <countrian1> ruler, <ruler1>, was killed by an assassin. The country is"
                      " mourning his death.",
                 prob=0.02)
event1_14 = dict(text="A strange infectious disease has broken out in <cap1>. Some citizens are"
                      " fleeing the city. There are already several dead.",
                 prob=0.02)
event1_15 = dict(text="In <country1>, there have recently been problems regarding the distribution"
                      " of food to the remote areas. The people expect the government to act.",
                 prob=0.02)
event1_16 = dict(text="A <countrian1> train has derailed. There are many dead and wounded.",
                 prob=0.02)
event1_17 = dict(text="Last season's exceptionally good harvest has proved a boost to the <countrian1>"
                      " economy.",
                 prob=0.02)
event1_18 = dict(text="Last season's exceptionally bad harvest has proved an issue to the <countrian1>"
                      " economy.",
                 prob=0.02)
event1_19 = dict(text="Farmers of <country1> are protesting against the government. They demand"
                      " more subsidies from the state.",
                 prob=0.02)
event1_20 = dict(text="There was a strike of police forces in <country1>. They demand higher wages.",
                 prob=0.02)

# How to implement for example: <country1>['stability'] -= 1?
# Also, introduce rank of importance to events.

# Events in which two countries get affected.

event2_1 = dict(text="The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                     " seemed to understand eachother well and wish to cooperate where possible.",
                prob=0.02)
event2_2 = dict(text="There was a conflict on the border between <country1> and <country2bordering1>. It started with"
                     " two antagonizing peasants and broadened to the scope of whole villages.",
                prob=0.02)
event2_3 = dict(text="A <countrian1> politician has insulted <ruler2>, the <countrian2> ruler, and disapproved his"
                     " recent policies.",
                prob=0.02)
event2_4 = dict(text="There was a terrorist attack in <country1>. The assassin is a <countrian2> man called"
                     " <man2>. Several innocent citizens died. The criminal got shot by police officers.",
                prob=0.02)
event2_5 = dict(text="A small <countrian1> airplane has crashed while crossing <countrian2> territory. Few passengers"
                     " died on the spot, one miraculously survived.",
                prob=0.02)
event2_6 = dict(text="A <countrian1> automobile company is making huge profits from export to <country2>.",
                prob=0.02)
event2_7 = dict(text="There seems to be much interest in <country1> for the culture and language of <country2> lately."
                     " Cinemas in <cap1> display movies of <countrian2> production regularly nowadays.",
                prob=0.02)
event2_8 = dict(text="The foreign ministers of <country1> and <country2> have met in <cap1>. They"
                     " didn't go along very well and the whole meeting felt forced and out of place.",
                prob=0.02)
event2_9 = dict(text="A dangerous storm has passed over <country1> and <country2bordering1>. There are dozens of"
                     " casualties in both countries.",
                prob=0.02)
event2_10 = dict(text="A small <countrian1> airplane has crashed while crossing <countrian2> territory. The few"
                      " passengers were unfortunately all killed on the spot.",
                 prob=0.02)

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

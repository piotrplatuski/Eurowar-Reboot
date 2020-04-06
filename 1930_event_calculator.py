import Events
import Countries
import random
import numpy
from mimesis import Person
from mimesis.enums import Gender


def one_country_events(nb=1):
    """Prints some."""
    selection = numpy.random.choice(Events.events1, nb, False, Events.events1_prob)
    result = []
    for event in selection:
        event = event.copy()
        country1 = random.choice(Countries.countries)
        if country1['name'] == 'Romania':
            event['text'] = str.replace(event['text'], '<man1>', 'some Romanian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Romanian woman')
        elif country1['name'] == 'Yugoslavia':
            event['text'] = str.replace(event['text'], '<man1>', 'some Yugoslavian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Yugoslavian woman')
        elif country1['name'] == 'Lithuania':
            event['text'] = str.replace(event['text'], '<man1>', 'some Lithuanian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Lithuanian woman')
        elif country1['name'] == 'Bulgaria':
            event['text'] = str.replace(event['text'], '<man1>', 'some Bulgarian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Bulgarian woman')
        else:
            person1 = Person(country1['gen'])
            event['text'] = str.replace(event['text'], '<man1>', person1.full_name(gender=Gender.MALE))
            event['text'] = str.replace(event['text'], '<woman1>', person1.full_name(gender=Gender.FEMALE))

        event['text'] = str.replace(event['text'], '<country1>', country1['name'])
        event['text'] = str.replace(event['text'], '<countrian1>', country1['conj'])
        event['text'] = str.replace(event['text'], '<ruler1>', country1['ruler'])
        event['text'] = str.replace(event['text'], '<cap1>', country1['capital'])

        result.append(event['text'])

    return result


def two_countries_events(nb=1):
    """Prints some."""
    selection = numpy.random.choice(Events.events2, nb, False, Events.events2_prob)
    result = []
    for event in selection:
        event = event.copy()
        chosen_countries = tuple(numpy.random.choice(Countries.countries, len(Countries.countries), False))
        country1 = chosen_countries[0]
        country2 = chosen_countries[1]

        if country1['name'] == 'Romania':
            event['text'] = str.replace(event['text'], '<man1>', 'some Romanian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Romanian woman')
        elif country1['name'] == 'Yugoslavia':
            event['text'] = str.replace(event['text'], '<man1>', 'some Yugoslavian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Yugoslavian woman')
        elif country1['name'] == 'Lithuania':
            event['text'] = str.replace(event['text'], '<man1>', 'some Lithuanian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Lithuanian woman')
        elif country1['name'] == 'Bulgaria':
            event['text'] = str.replace(event['text'], '<man1>', 'some Bulgarian man')
            event['text'] = str.replace(event['text'], '<woman1>', 'some Bulgarian woman')
        else:
            person1 = Person(country1['gen'])
            event['text'] = str.replace(event['text'], '<man1>', person1.full_name(gender=Gender.MALE))
            event['text'] = str.replace(event['text'], '<woman1>', person1.full_name(gender=Gender.FEMALE))

        if country2['name'] == 'Romania':
            event['text'] = str.replace(event['text'], '<man2>', 'some Romanian man')
            event['text'] = str.replace(event['text'], '<woman2>', 'some Romanian woman')
        elif country2['name'] == 'Yugoslavia':
            event['text'] = str.replace(event['text'], '<man2>', 'some Yugoslavian man')
            event['text'] = str.replace(event['text'], '<woman2>', 'some Yugoslavian woman')
        elif country2['name'] == 'Lithuania':
            event['text'] = str.replace(event['text'], '<man2>', 'some Lithuanian man')
            event['text'] = str.replace(event['text'], '<woman2>', 'some Lithuanian woman')
        elif country2['name'] == 'Bulgaria':
            event['text'] = str.replace(event['text'], '<man2>', 'some Bulgarian man')
            event['text'] = str.replace(event['text'], '<woman2>', 'some Bulgarian woman')
        else:
            person2 = Person(country2['gen'])
            event['text'] = str.replace(event['text'], '<man2>', person2.full_name(gender=Gender.MALE))
            event['text'] = str.replace(event['text'], '<woman2>', person2.full_name(gender=Gender.FEMALE))

        event['text'] = str.replace(event['text'], '<country1>', country1['name'])
        event['text'] = str.replace(event['text'], '<country2>', country2['name'])
        event['text'] = str.replace(event['text'], '<countrian1>', country1['conj'])
        event['text'] = str.replace(event['text'], '<countrian2>', country2['conj'])
        event['text'] = str.replace(event['text'], '<ruler1>', country1['ruler'])
        event['text'] = str.replace(event['text'], '<ruler2>', country2['ruler'])
        event['text'] = str.replace(event['text'], '<cap1>', country1['capital'])
        event['text'] = str.replace(event['text'], '<cap2>', country2['capital'])
        event['text'] = str.replace(event['text'], '<country2bordering1>', list(country1['bordering'])[0])

        result.append(event['text'])

    return result


def battle(attacker, defender, from_province, to_province):
    """Calculates the outcomes of battles."""

import event_texts as ev
import random
import american_map as map

def generate_events(year=0):
    amount = random.choices([5,6,7,8,9,10], [10,15,25,25,15,10])[0]
    event_texts = []
    for i in range(1, amount):
        current_event = random.choices(ev.all, ev.all_probs)[0]
        satisfying_countries = {country for country in map.all_countries} ## if current_event.check_conditions(country
        current_countries = random.choices(satisfying_countries, k=current_event.get_amount_countries())
        current_text = current_event.fill_in_text()
        event_texts.append(current_text)

    print('events:')
    for text in event_texts:
        print(text)
        print('/n')

print(generate_events(1996))


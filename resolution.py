import event_texts as ev
import random
import american_map as map

def generate_events(year=0):
    amount = random.choices([5,6,7,8,9,10], [10,15,25,25,15,10])[0]
    event_texts = []
    unused_events = ev.all.copy()
    unused_events_probs = ev.all_probs.copy()
    for i in range(1, amount+1):
        current_event = random.choices(unused_events, unused_events_probs)[0]
        current_event_index = unused_events.index(current_event)
        unused_events_probs.pop(current_event_index)
        unused_events.pop(current_event_index)
        satisfying_countries = [country for country in map.all_countries] ## if current_event.check_conditions(country
        current_countries = random.choices(satisfying_countries, k=current_event.get_amount_countries())
        current_text = current_event.fill_in_text(set(current_countries))
        event_texts.append(current_text)

    output = 'Amount of events: ' + str(amount)
    for i in range(0, amount):
        output += '\n' + str(i+1) + ': ' + event_texts[i]
    return output

print(generate_events(1996))


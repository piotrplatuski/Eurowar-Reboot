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


effect_variables = {'{country1}', '{prov1}', '{ruler1}'
                    '{country2}', '{prov2}', '{ruler2}'
                    '{country3}', '{prov3}', '{ruler3}'
                    '{country4}', '{prov4}', '{ruler4}'
                    '{prov0}'}


def fire_event(event, countries):
    elements = event.get_effects().split(', ')
    elem_list = []
    for j in range(0, len(elements)):
        elem_list.append([])
        elem_list[j] = elements[j].split(' ')
    new_list = [item for sublist in elem_list for item in sublist]
    indeces = []
    for ef_var in effect_variables:
        if ef_var in new_list:
            indeces.append(new_list.index(ef_var))
    indeces.sort()
    indeces.append(len(new_list)-1)

    for i in range(0, len(indeces)):

        if new_list[indeces[i]] == '{prov0}':
            interval = (indeces[i], indeces[i+1])
            for pos in range(interval[0], interval[1]):
                prov = random.choice(map.neutral_provs)
                if new_list[pos] == 'name':
                    prov.set_name(int(new_list[pos+1]))
                if new_list[pos] == 'building':
                    prov.add_building(int(new_list[pos+1]))

        if new_list[indeces[i]] == '{country1}':
            interval = (indeces[i], indeces[i+1])
            for pos in range(interval[0], interval[1]):
                if new_list[pos] == 'economy':
                    countries[0].change_balance(int(new_list[pos+1]))
                if new_list[pos] == 'stability':
                    countries[0].change_stability(int(new_list[pos+1]))

        if new_list[indeces[i]] == '{prov1}':
            interval = (indeces[i], indeces[i+1])
            for pos in range(interval[0], interval[1]):
                prov = countries[0].random_province()
                if new_list[pos] == 'name':
                    prov.set_name(int(new_list[pos+1]))
                if new_list[pos] == 'building':
                    prov.add_building(int(new_list[pos+1]))

        if new_list[indeces[i]] == '{ruler1}':
            current_ruler = countries[0].get_ruler()
            interval = (indeces[i], indeces[i+1])
            for pos in range(interval[0], interval[1]):
                if new_list[pos] == 'fname':
                    current_ruler.set_first_name(new_list[pos+1])
                    countries[0].set_ruler(current_ruler)
                if new_list[pos] == 'lname':
                    current_ruler.set_last_name(new_list[pos+1])
                    countries[0].set_ruler(current_ruler)
                if new_list[pos] == 'nickname':
                    current_ruler.set_nickname(new_list[pos + 1])
                    countries[0].set_ruler(current_ruler)
                if new_list[pos] == 'type':
                    countries[0].set_ruler_type(new_list[pos+1])
                if new_list[pos] == 'birthyear':
                    current_ruler.set_birthyear(new_list[pos+1])
                    countries[0].set_ruler(current_ruler)


print(map.chicago.get_ruler().full_name())
print(map.chicago.get_balance())
print(map.chicago.get_stability())
print('____________-')
print(fire_event(ev.ev1_2, [map.chicago]))
print(map.chicago.get_ruler().full_name())
print(map.chicago.get_balance())
print(map.chicago.get_stability())



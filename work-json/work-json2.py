import json

with open('states.json') as f:
    data = json.load(f)                 # loaded JSON file into a Python object

for state in data['states']:
    # print(state)
    # print(state['name'], state['abbreviation'])
    del state['area_codes']

with open('new_states.json', 'w') as f:               # 'w': argument -> write
    json.dump(data, f, indent=2)                                # f = file that we opened
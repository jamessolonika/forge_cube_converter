import json

filename = 'default_general_values.json'

default_values = {
    'sort_method': 1,
    'want_draft': True,
    'want_sealed': False,
    'want_automove': True,
    'not_found_action': 1,
    'not_found_ask_each_time': False,
}

with open(filename,'w') as f_obj:
    json.dump(default_values,f_obj)



filename = 'default_draft_values.json'

default_values = {
    'singleton': True,
    'booster': '15 Any',
    'numpacks': 3,
    'landsetcode': 'UST'
}

with open(filename,'w') as f_obj:
    json.dump(default_values,f_obj)



filename = 'default_sealed_values.json'

default_values = {
    'ignorerarity': True,
    'booster': '15 Any',
    'numpacks': 3,
    'landsetcode': 'UST'
}

with open(filename,'w') as f_obj:
    json.dump(default_values,f_obj)
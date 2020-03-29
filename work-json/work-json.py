import json

""" JSON (JavaScript Object Notation) = very common data format for storing some information
    Inspired from JavaScript but it is now independent of any language
    -> almost every language has libraries for parsing and generating JSON data """

# each people object has 4 keys; "name", "phone", "emails" and "has_licence"
people_string = """
{
    "people": [                 
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_licence": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_licence": true
        }
    ]
}
"""
# load this into python object so that we can work with the data easily

data = json.loads(people_string)
# print(type(data))                   # python dictionary (JSON object to dict)
# print(data)
# print(type(data['people']))         # list (array to list)

"""     JSON Python conversion table 

        JSON            Python
        object          dict
        array           list
        string          str
        number (int)    int
        number (real)   float
        true            True
        false           False
        null            None
"""

for person in data['people']:
    # print(person)
    # print(person["name"])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)     # new JSON string no longer contains phone numbers for each person
print(new_string)                                           # indent is important for formatting, number of indentions per item
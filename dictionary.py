acronyms_list = ["LOL", "IDK", "TBH"]
translations_list = ["laugh out loud", "I don't know", "to be honest"]

# we can create a list of acronyms and their translation which could be problemmatic when ned to delete or add new items
# So we can make use of dictionary with the key:value pair

# Dictionary of strings to strings
acronyms = {"LOL": "laugh out loud",
            "IDK": "I don't know", "TBH": "to be honest"}
print("printing whole dictionary", acronyms)
print(acronyms["IDK"])

# Dictionary of strings to number
menu = {"soup": 5, "salad": 6}
print(menu["salad"])

# Dictionary of anything
my_dict = {10: 'hello', 4: 0.6}
print(my_dict[4])

# Dictionary is updated in the same way as added

my_dict[4] = "four"
print("dictionary of anything", my_dict)

# Delete the value from Dictionary
del my_dict[10]
print("after deleting the value from dictionary", my_dict)


value = my_dict.get(10)
# KEYError if key does't exist
if value:
    del my_dict[10]
else:
    print("Key does't exist")


print(value)

# Dictionary of Lists

_menus = {"Breakfast": ["Egg Sandwitch", "Bagel",
                        "Coffee"], "Lunch": ["BLT", "PB&J", "Roti Dal"], "Dinner": ["Soup", "Salad", "Spaghetti", "Taco"]}

for name, menu in _menus.items():
    print(name, ':', menu)

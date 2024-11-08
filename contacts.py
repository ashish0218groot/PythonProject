# Parse the nested contacts dictionary

contacts = {
    'number': 4,
    'students': [
        {'name': "Bhim", 'email': "bhim@g.com"},
        {'name': "Himanshu", 'email': "himanshu@g.com"},
        {'name': "Sandeep", 'email': "sandeep@g.com"}
    ]
}

print("Student emails")
for student in contacts['students']:
    print(student['email'])

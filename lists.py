# Learning list items

# acronyms is the list object and append is the method
acronyms = ['IDH', 'FMH', 'BBN']

acronyms.append('ACR')
acronyms.append('MDB')

print(acronyms)

# Remove the list items
acronyms.remove('MDB')

#  OR delete by index

del acronyms[2]

print(acronyms)


# Checking if the item is in the list
if 1 in [1, 2, 3, 4, 5]:
    print('True')

word = 'ACR'

if word in acronyms:
    print('True')


# for loop to print each item in the list
for acronym in acronyms:
    print(acronym)

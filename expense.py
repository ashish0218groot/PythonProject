# calculating he sum of expense

expenses = [10.5, 43, 55, 23, 23.64, 33]

total_expense = 0

for expense in expenses:
    total_expense += expense

print('You spent $', total_expense, sep='')

# Using sum

total = sum(expenses)
print('You spent $', total, sep='')

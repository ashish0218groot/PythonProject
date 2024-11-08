# Using range

for i in range(7):
    print('range value:', i, sep='')


# *************

# Example
total = 0
expenses = []

num_expenses = int(input("Enter # of expenses: "))

for i in range(num_expenses):
    expenses.append(int(input("Enter expense: ")))

total = sum(expenses)

print("The total expense is : ", total)

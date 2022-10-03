# The Lost Budget
# 29 September 2022
# CTI-110 P1HW2 - Travel Expense
# William Kinchen

# user enter Budget
# user enter destination
# user enter gas amount
# user enter amount spent on accomodations
# user enter amount spent on food
# add total expenses
# subtract expenses from Budget
# Display final Balance

# input
budget = int(input('Enter Budget Now:'))
destination = (input('Enter Your Destination:'))
gas = int(input('Enter Gas Amount:'))
accomodations = int(input('Enter Amount on Accomodations:'))
food = int(input('Enter Your Food Expenses:'))

# process
expense = gas + accomodations + food
balance = budget - expense

#output
print('----------Travel Expenses----------')
print('Location:', destination)
print('Initial Budget:', budget)
print('')
print('Fuel:', gas)
print('Accomodation:', accomodations)
print('Food:', food)
print('')
print('Remaining Balance', balance)
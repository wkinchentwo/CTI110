# P2HW1
# 10 OCT 2022
# CTI-110 P2HW1 - Travel
# William Kinchen


print('This program calculates and displays travel expenses')
print()
budget = float(input('Enter Budget: '))
print()
destination = input('Enter your travel destination: ')
print()
fuel = float(input('How much do you think you will spend on gas? '))
print()
hotel_stay = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
food = float(input('Last, how much do you need for food? '))
print()
print('----------Travel Expenses----------')
print(f'Location:              {destination}')
print(f'Initial Budget:        ${budget:.2f}')
print(f'Fuel:                  ${fuel:.2f}')
print(f'Accomodation:          ${hotel_stay:.2f}')
print(f'Food:                  ${food:.2f}')
print('-----------------------------------')
print()
print(f'Remaining Balance:     ${(budget-(fuel+hotel_stay+food))}')

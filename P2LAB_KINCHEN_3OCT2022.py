#input
gas_cost = 3.1599
mile20 = 20.0
mile75 = 75.0
mile500 = 500.0

#output
print(f'Your cost per gallon for 20 miles is: {gas_cost:.2f}')
print(f'Your cost per gallon for 75 miles is: {(mile75/mile20)*gas_cost:.2f}')
print(f'Your cost per gallon for 500 miles is: {(mile500/mile20)*gas_cost:.2f}')

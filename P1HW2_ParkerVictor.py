# Calculates and displays travel expenses
# 22 September 2022
# CTI-110 P1HW2 - Travel Expense
# Parker, Victor
#


print('This program calculates and displays travel expenses\n')

print('Enter Budget:')
budget = int(input())
print(' ')
print('Enter your travel destination:')
user_loc = input()
print(' ')
print('How much do you think you will spend on gas?')
gas = int(input())
print(' ')
print('Approximately, how much will you need for accomodation/hotel?')
user_hotel = int(input())
print(' ')
print('Last, how much do you need for food?')
user_food = int(input())
print(' ')
print('------------Travel Expenses------------')
print('Location:', user_loc)
print('Initial Budget:', float(budget))
print(' ')
print('Fuel:', float(gas))
print('Accomodation:', float(user_hotel))
print('Food:', float(user_food))
print(' ')

total = (gas + user_hotel + user_food)
print('Remaining Balance:', float(budget-total))

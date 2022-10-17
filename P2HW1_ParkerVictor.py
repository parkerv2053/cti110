# Calculates and displays travel expenses, simplified
# 5 October 2022
# CTI-110 P1HW2 - Travel Expense
# Parker, Victor
#


print('This program calculates and displays travel expenses\n')

#this section covers the user input and their formatting
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

#This section displays the input from tyhe user and organizes it
print('------------Travel Expenses------------')
print(f'Location:           {user_loc}')
print(f'Initial Budget:     ${budget:.1f}')
print(f'Fuel:               ${gas:.1f}')
print(f'Accomodation:       ${user_hotel:.1f}')
print(f'Food:               ${user_food:.1f}')
print('---------------------------------------\n')

#This is the end result that displays the math
remaining = (budget) - (gas + user_hotel + user_food)
print(f'Remaining Balance:  ${remaining:.1f}')

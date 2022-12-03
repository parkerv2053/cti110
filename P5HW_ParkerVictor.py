# A brief description of the project
# 23 November 2022
# CTI-110 P5HW2 - Math Quiz
# Victor Parker
#
   
import random

def main_menu():
    title = 'Welcome to Math Quiz!!!'
    title1 = '   MAIN MENU   '
    print(title)
    print('-' * len(title))
    print(title1)
    print('-' * len(title))

def menu_shown():
    menu_list = ['1. Adding Random Numbers', '2. Subrtracting Random Numbers', '3. Exit']
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

def get_user_selection():
    user_selection = int(input('Please choose one of the menu options:'))
    while user_selection > 4 or user_selection <= 0:
        print('Invalid Input')
        user_selection = int(input('Please choose one of the menu options:'))
    else:
        return user_selection



def addtionprob():
    guess = 1
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    add = first + second
    print(first)
    print(f'+{second}')
    userans = int(input())
    while userans != add:
        if userans < add:
            guess += 1
            print('Your answer is too low\nTry Again!')
            userans = int(input())            
        else:
            guess += 1
            print('Your answer is too high\nTry Again!')
            userans = int(input())
    else:
        if guess != 1:
            print('Contgradulations!!!! Your answer is correct....')
            print(f'Number of guesses: {guess}')
            return main()
        else:
            guess == 1
            print('Contgradulations!!!! Your answer is correct....')
            print(f'Number of guesses: {guess}')
            return main()


def subtractprob():
    guess = 1
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    sub = first - second
    print(first)
    print(f'-{second}')
    userans = int(input())  
    while  userans != sub:
        if userans < sub:
            guess += 1
            print('Your answer is too low')
            userans = int(input('Try Again!'))
        else:
            guess += 1
            print('Your answer is too high')
            userans = int(input('Try Again!'))
    else:
        if guess != 1:
            guess -= 1
            print('Contgradulations!!!! Your answer is correct....')
            print(f'Number of guesses: {guess}')
            return main()
        else:
            guess == 1
            print('Contgradulations!!!! Your answer is correct....')
            print(f'Number of guesses: {guess}')
            return main()



def main():
    main_menu()
    menu_shown()
    
    choice = get_user_selection()
    if choice == 1:
        addtionprob()
    elif choice == 2:
        subtractprob()
    else:
        print('Thank you for playing...\nBye!!')
main()

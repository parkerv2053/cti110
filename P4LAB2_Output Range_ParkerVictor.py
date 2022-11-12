number_one = int(input())
number_two = int(input())

if number_one <= number_two:
    index = number_one
    while (index <= number_two):
        print(index, end= ' ')
        index += 5
    print()
else:
    print("Second integer can't be less than the first.")

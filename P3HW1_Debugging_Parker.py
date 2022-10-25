# CTI-110
# P3HW1 - Debugging
# Parker, Victor
# 24 October 2022


# This program takes a number grade , determines average and displays letter grade for average.

# This section had missing underscores, mispelling, wrong number scheme. I added floats to each just to
# make things easier as we go forward
# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
# This was missing a comma, underscore as well as all of mod_6
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
# This had the wrong functions for the max, avg wasn't even done, grades wasn't spelled how it should be.
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = (sum / (len(grades)))

print('------------Results------------')
print(f'Lowest Grade:      {low}')
print(f'Hightest Grade:    {high}')
print(f'Sum of Grades:     {sum}')
print(f'Average:           {avg:.2f}')
print('----------------------------------------')

# determine letter grade for average
# this one took a while to work but was easy in comparison to getting the print function to work correctly.
# I know there are cleaner ways to do this but this was the simplest and more effective I could do.

if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')
 
elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F') # TO DO: finish this: completed!!!






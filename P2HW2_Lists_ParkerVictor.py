  # CTI-110
  # P2HW2 - List
  # Parker, Victor
  # 5 October 2022
  # This program is to manage and complile a list of grades to allow better analytical requests
   
   
   
print('Enter grade for Module 1:')
module1 = float(input())
print('Enter grade for Module 2:')
module2 = float(input())
print('Enter grade for Module 3:')
module3 = float(input())
print('Enter grade for Module 4:')
module4= float(input())
print('Enter grade for Module 5:')
module5= float(input())
print('Enter grade for Module 6:\n')
module6= float(input())

grade_in_class = [module1, module2, module3, module4, module5, module6]

print('------------Results------------')
print(f'Lowest Grade:        {(min(grade_in_class)):.1f}')
print(f'Highest Grade:       {(max(grade_in_class)):.1f}')
print(f'Sum of Grades:       {(sum(grade_in_class)):.1f}')
print(f'Average:             {((sum(grade_in_class))/(len(grade_in_class))):.2f}')
print('----------------------------------------')
# CTI-110
# P3HW2 - Salary
# Parker, Victor
# 25 October 2022
#

# input section.
# name = input(name)
# hours = input( hours worked)
# payrate for emplyee = input(payrate)

employee_name = input("Enter employee's name: ")
hours_worked = float(input('Enter number of hours worked: '))
payrate = float(input("Enter employee's pay rate: "))

# fomula and equation section
# hours work = hour_worked:.1f
# Pay Rate = payrate:.1f
# Over time = ( if hours_worked > 40 then hours_worked - 40 else Over time == 0)
# Overtimepay = ((Pay Rate/2) + Pay Rate) * Over time
# Regular hour pay = (hours work - overtime) * Pay Rate
# Gross Pay = Regular hour pay + Overtimepay

if hours_worked > 40:
    overtime = (hours_worked - 40)
else:
    overtime = float(0)
    
overtime_pay = ((payrate/2) + payrate) * overtime
reghourpay = (hours_worked - overtime) * payrate
grosspay = (reghourpay + overtime_pay)

print('-------------------------------------------')
print(f'Employee name:     {employee_name}\n')
print("Hours Worked     Pay Rate    OverTime         OverTime Pay       RegHour Pay       Gross Pay")
print('----------------------------------------------------------------------------------------------')
print(f'{hours_worked:<16.1f} {payrate:<11.1f} {overtime:<17.1f}{overtime_pay:<18.2f} ${reghourpay:<16.2f} ${grosspay:<-20.2f}')
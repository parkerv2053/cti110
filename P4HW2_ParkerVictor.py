# CTI-110
# P4HW2 - Salary Calculator
# Parker, Victor
# 14 November 2022
#

#Variable starts and lists
word = str('None') #None kept breaking my code so had to make a keyword
employee = ['None', 'none'] #honestly I just put none in there just incase a discrepancy happened
OT = [] #overtime list
regH = [] #regular hours pay list
gross = [] # gross income list
employed = 0 #used to cound the entrys, tend it be off count, so used another section to off set it.

#first employee set (had difficulty getting the names reentered)
employee_name = input("Enter employee's name or \"None\" to terminate:")

#begining of the loop
#employ count must be greater than or equal to 0 and not the word None
while (employed >= 0) and (employee_name != word):
    employed += 1 # addes 1 tot he employed count
    if employee_name in employee: #the input must be in the list then this loop begins. (found it when experimenting in ide)
        employee_name = input("Enter employee's name or \"None\" to terminate:") #enters new employee name
        if employee_name != word: #as long as its not the word None 
            employee.append(employee_name) #adds name to list itll make the loop start over again.
            #variable input
            hours_worked = float(input(f'How many hours did {employee_name} worked? '))
            payrate = float(input(f"What is {employee_name}'s pay rate? ")) 
            # worked hours is greater than 40 then subtract the hours worked from 40 to get overtime
            # otherwise overtime is 0
            if hours_worked > 40:
                overtime = (hours_worked - 40)
            else:
                overtime = float(0)
            #overtime = (1.5 times the payrate then multiply the overtime hours.)
            #added overtime to OT list
            overtime_pay = ((payrate/2) + payrate) * overtime
            OT.append(overtime_pay)
            #subtract the over time from hours worked (rp = (H-O)*pr)
            #add to list for regular hour pay
            reghourpay = (hours_worked - overtime) * payrate
            regH.append(reghourpay)
            #groos pay is adding regpay and overtime pay (gp = rp + ot)
            #add to the gross list
            grosspay = (reghourpay + overtime_pay)
            gross.append(grosspay)
            print('-------------------------------------------')
            print(f'Employee name:     {employee_name}\n')
            print("Hours Worked     Pay Rate    OverTime         OverTime Pay       RegHour Pay       Gross Pay")
            print('----------------------------------------------------------------------------------------------')
            print(f'{hours_worked:<16.1f} {payrate:<11.1f} {overtime:<17.1f}{overtime_pay:<18.2f} ${reghourpay:<16.2f} ${grosspay:<-20.2f}')
        else: #for when None is entered
            employed -= 1 #corrects the over count when None is entered and counted
            print(f'Total number of employees entered:{employed}') #refers to employed count
            print(f'Total amount payed for overtime: ${sum(OT)}') #add everything in the Overtime list
            print(f'Total amount payed for regular hour: ${sum(regH)}') #adds everything in the Regpay list
            print(f'Total amount payed in gross: ${sum(gross)}')    #adds everything in the gross list 
    elif (employee_name not in employee) and (employee_name != word): #deals with the inital name to start the loop
        employee.append(employee_name) #adds the name to the list to continue loop at top
        #same patterned as before
        hours_worked = float(input(f'How many hours did {employee_name} worked? '))
        payrate = float(input(f"What is {employee_name}'s pay rate? "))
        if hours_worked > 40:
            overtime = (hours_worked - 40)
        else:
            overtime = float(0)
        overtime_pay = ((payrate/2) + payrate) * overtime
        OT.append(overtime_pay)
        reghourpay = (hours_worked - overtime) * payrate
        regH.append(reghourpay)
        grosspay = (reghourpay + overtime_pay)
        gross.append(grosspay)
        print('-------------------------------------------')
        print(f'Employee name:     {employee_name}\n')
        print("Hours Worked     Pay Rate    OverTime         OverTime Pay       RegHour Pay       Gross Pay")
        print('----------------------------------------------------------------------------------------------')
        print(f'{hours_worked:<16.1f} {payrate:<11.1f} {overtime:<17.1f}{overtime_pay:<18.2f} ${reghourpay:<16.2f} ${grosspay:<-20.2f}')
    else: #ends it
        print()
else: #ends it
    print()


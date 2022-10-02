#this is the car's gas milege inputed
milage = float(input())

#this is the cost of gas inputed
cost_gas = float(input())

#formula for costs
your_value1 = float((20.0 / milage) * cost_gas)
your_value2 = float((75.0 / milage) * cost_gas)
your_value3 = float((500.0 / milage) * cost_gas)

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = pay = hours * rate
if hours > 40 :
    overtime = (hours - 40) * rate * 1.5
    pay = 40 * rate + overtime
print("Pay:", pay)

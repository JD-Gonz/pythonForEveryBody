# Exercise 2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully
# by printing a message and exiting the program.

try :
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))    
except :
    print("Error, please enter numeric input")
    quit()
    
pay = pay = hours * rate
if hours > 40 :
    overtime = (hours - 40) * rate * 1.5
    pay = 40 * rate + overtime
print("Pay:", pay)

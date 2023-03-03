# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
# and create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate) :
    pay = hours * rate
    if hours > 40 :
        overtime = (hours - 40) * rate * 1.5
        return 40 * rate + overtime
    else :
        return pay

try :
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))    
except :
    print("Error, please enter numeric input")
    quit()    
    
print("Pay:", computepay(hours, rate))


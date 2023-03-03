# Exercise 2: Write another program that prompts for a list of numbers
# and at the end prints out both the maximum and minimum of the numbers.

min = None
max = None
while True :
    try :
        inputString = input("Enter a number: ")
        num = int(inputString)
    except :
        if inputString == "done" :
            break
        else :
            print("Invalid input")
            continue
    if min == None  :
        min = num
        max = num
    elif min > num :
        min = num
    elif max < num :
        max = num

print("Maximum is", max)
print("Minimum is", min)   
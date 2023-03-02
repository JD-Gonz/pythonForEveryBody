# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
try :
    score = float(input("Enter score: "))
except :
    score = -1
    
if score < 1 and score >= 0 :    
    if score >= .9 :
        print("A")
    elif score >= .8 :
        print("B")
    elif score >= .7 :
        print("C")
    elif score >= .6 :
        print("D")
    else :
        print("F")
else :
    print("Bad Score")
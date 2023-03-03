# Exercise 7: Rewrite the grade program from the previous chapter 
# using a function called computegrade that takes a score as its parameter
# and returns a grade as a string.
def computegrade(score) :
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

try :
    score = float(input("Enter score: "))
except :
    score = -1

computegrade(score)
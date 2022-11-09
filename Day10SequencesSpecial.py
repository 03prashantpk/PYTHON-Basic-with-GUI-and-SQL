import re
# Enter Question number to run
question_no = int(input("Enter Question number: "))

# Question 1  \A (Check if special char is present at the starting string)
if question_no == 1:

    strings = input("Enter a string: ") # my name is khan
    find = input("What to find?: ") # my

    x = re.findall("\A%s"%(find), strings)

    if x:
        print("Yes, Match Found")
    else:
        print("No match")


# Question 2 \b (Check if special char is present at end of the string)
elif question_no == 2:

    strings = input("Enter a string: ")

    #find = input("What to find?: ")
    x = re.findall(r"foot\b", strings)

    if x:
        print("Yes, there is one match!", x)
    else:
        print("No match")


# Question 3 \B (Check if special char is present at but not at
# the starting or ending  of the string)
elif question_no == 3:
    strings = input("Enter a string: ")

    #find = input("What to find?: ")
    x = re.findall(r"foot\B", strings)

    if x:
        print("Yes, there is one match!", x)
    else:
        print("No match")


# Returns a match where the string contains digits (numbers from 0-9)
elif question_no == 4:
    strings = input("Enter a string: ")

    #find = input("What to find?: ")
    x = re.findall("\d", strings)

    if x:
        count = (len(x))
        print("Yes, there are",count,"match!", x)
        
    else:
        print("No match")


# Returns a match where the string DOES NOT contain digits
elif question_no == 5:
    strings = input("Enter a string: ")

    #find = input("What to find?: ")
    x = re.findall("\D", strings)

    if x:
        print("Yes, there is one match!", x)
    else:
        print("No match")




# Day 2 Questions
print("\nDay 2 Questions")
print("Available Question No's are 1, 2 and 3 \n")

show_question = int(input("Enter Q.no: "))

if show_question == 1:
    # Question 1----------------------------------------------------

    print("\nSHOWING QUESTION 1 Now\n")
    '''
    Given 'd' dollars, the future value of this money when compounded yearly at a rate of 'r'
    percentage interest for 'y' years is d(1+0.01r)y. WAP to realize the given formula taking the input at run-time.

    '''

    # Formula d(1+0.01r)y
    amount = int(input("Enter Dollar: "))
    year = int(input("Enter Year: "))
    rate = int(input("Enter Interest Rate: "))
    compound_money = amount*(1+0.01*rate)*year

    print("Total Future Value ", compound_money)
    print("\n")


elif show_question == 2:
    # Question 2----------------------------------------------------

    print("\nSHOWING QUESTION 2 Now\n")
    '''
    WAP to obtain the following output:
    OUTPUT Formate
    Enter the name: Moin Hasan
    Enter the age: 34
    Moin Hasan is 34 years old.
    '''

    name = input("Enter the Name: ")
    age = int(input("Enter the Age: "))
    print(name, "is", age, "years old.")
    print("\n")

elif show_question == 3:
    # Question 3----------------------------------------------------

    print("\nSHOWING QUESTION 3 Now\n")
    '''
    The distance between two point (x0,y0) and (x1,y1) is sqrt((x0-x1)2+(y0-y1)2).
    WAP to realize the given distance formula by taking the coordinate as the input form the user.

    Expontential Operator: **
    '''
    # Importing maths py
    import math

    # Coordinate x1 and y1 values   User Inputs
    x1 = int(input("Enter value of X1: "))
    y1 = int(input("Enter value of Y1: "))

    # Coordinate x2 and y2 values   User Inputs
    x2 = int(input("Enter value of X2: "))
    y2 = int(input("Enter value of Y2: "))

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("\nDistance between the given coordinate is:", distance)
    print("\n")

else:
    print("Wrong input or you reach to the end.\nPlease Check Question No's")

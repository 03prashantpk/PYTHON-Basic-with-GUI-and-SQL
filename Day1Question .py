print("\nDay 1 Questions")
print("Available Question No's are 1, 2, 3 and 4 \n")

show_question = int(input("Enter Q.no: "))


if show_question == 1:
# Question 1----------------------------------------------------

    print("\nSHOWING QUESTION 1 Now\n")
    '''
    Q1. There are 5280 feet in a mile. WAS that calculate and print the number of 
    feet in "n" miles. Take the Value of "n" form user un run time
    '''

    # 1 mile = 5280 feet
    mile = 5280

    # User Input for mile
    user_input = int(input("Enter number of Miles: "))

    # Printing total feets according to user input
    print("No of feet in", user_input, "are: ", user_input*mile)

elif show_question == 2:
# Question 2----------------------------------------------------
    print("\nSHOWING QUESTION 2 Now\n")
    '''
    Q2. WAPS to calculate and print the number of second in "h" hours, "m" minutes
    and "s" Seconds.
    '''

    # Common info
    sec = 60
    min = 60
    hours = 60*60

    # Hours input from users
    user_hours = int(input("Enter Hour: "))
    print("Converted Hours in Seconds", hours*user_hours, "\n")
    print("Converted Hours in Min", min*user_hours, "\n")



elif show_question == 3:
# Question 3----------------------------------------------------

    print("\nSHOWING QUESTION 3 Now\n")
    '''
    Q2. WAPS to Calculate the perimeter of a rectangle taking L & B From user.
    '''
    # Formula for perimeter of Rectangle = 2(l+b)

    len = int(input("Enter the Length: "))
    wid = int(input("Enter the Width: "))
    print("Perimeter of the Rectangle: ", 2 * (len + wid))


elif show_question == 4:
# Question 4----------------------------------------------------

    print("\nSHOWING QUESTION 3 Now\n")
    '''
    Q2. WAPS to Calculate the circumfrance of a circle by taking its radius as the input from user.
    '''
    # Formula for COC = 2*(22/7)*r
    circumfrance = 2*3.14

    # radius input from user
    radius = int(input("Enter the Radius: "))
    print("Circumfrance of the circle is", circumfrance*radius)

else: 
    print("wrong input or you reach to the end.")

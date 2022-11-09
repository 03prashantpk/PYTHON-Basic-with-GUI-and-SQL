# Day 4 Questions

# Question 1 - CI Calculation
print("\nDay 2 Questions")
print("Available Question No's are 1 , 2, 3 and 4 \n")

show_question = int(input("Enter Q.no: "))

if show_question == 1:
    ''' 
    An investor depostits $10,000 with the Get-Rich_Quick agency and receives a
    statement predicting the earnings on an annual percentage rate (APR) of 6% for
    a period of 5 years.

    WAP that prints the beginning principle and the interest earned for each year of the
    period. The program also prints the total amount earned and the final Principal.

    Output:
    Enter principal Amount: 10000
    Enter Rate: 6
    Enter Time Period: 5
    '''
    # Breaking line
    print("\nSHOWING QUESTION 1 Now\n")
    print("\n")

    # Program starts here...

    print("Enter Your details (All input must be of int type)\n")
    pricipal_ammount = int(input("Enter Principle Amount: "))
    rate_of_interest = int(input("Enter Rate: "))
    time_period = int(input("Enter Time Period: "))
    print("\n")

    for i in range(time_period+1):
        amount = (pricipal_ammount*rate_of_interest*time_period)/100
        print("Interest Amount After", i, " Year: ", amount)
        pricipal_ammount = pricipal_ammount+amount
        print("Total amount:", pricipal_ammount, "\n")


# Question 2 - Password Guessing
elif show_question == 2:
    ''' 
    Write a password guessing program to keep track of how many times the
    user has entered the password wrong. If it is more than 3 times, print
    "You have been denied access." and terminate the program. If the password
    is correct, print "You have successfully logged in." and terminate the
    program.
    '''

    print("\nSHOWING QUESTION 1 Now\n")
    print("\n")

    for i in range(0, 4):

        # Input Password
        password = input("Please Enter your Password: ")
        print("\n")

        # Assigned correct Password
        correct_password = "password"

        # Check if Password is correct
        if password == correct_password:
            print("Correct Password!")

            # If password is correct Break the loop
            break
        else:
            # Echo Entered Password is Wrong
            print("Entered Password is Wrong!")
            print("Try Again,", 3-i, "Attempt Remaining")

    # If Loop Range End the Program printing Access Denied!
    else:
        print("Access Denied!\n")

        print("Reset Password and Try Again\n")
        rest_password = int(input("Enter 0 to reset Password: "))
        print("\n")

        if rest_password == 0:
            print("Reset your Password")
            new_password = input("Enter New Password: ")

            for i in range(0, 1):

                # Input Password
                password = input("Please Enter your New Password: ")
                print("\n")

                # Check if Password is correct
                if password == new_password:
                    print("Correct Password!")

                    # If password is correct Break the loop
                    break
                else:
                    # Echo Entered Password is Wrong
                    print("Entered Password is Wrong!")
                    print(i, "Attempt Remaining")

            # If Loop Range End the Program printing Access Denied!
            else:
                print("Access Denied! For 24 hours\n")

# Question 3 - Printing Fizz, Buzz and FizzBuzz
elif show_question == 3:
    ''' 
    Write a Python program which iterates the integers from 1 to 50. For
    multiples of three print "Fizz" instead of the number and for the multiples
    of five print "Buzz". For numbers which are multiples of both three and five
    print "FizzBuzz"
    '''

    print("This Program will print Fizz, Buzz and FizzBuzz")
    for i in range(0, 50):
        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", "(", i, ")")
                continue
        elif i % 3 == 0:
                print("Fizz", "(", i, ")")
                continue
        elif i % 5 == 0:
                print("Buzz", "(", i, ")")
                continue
        print(i)


# Question 4 - Printing Fizz, Buzz and FizzBuzz
elif show_question == 4:
    ''' Write a Python program to print Alphabet patter of letter A
    '''

    '''
    result_str="";    
    for row in range(0,7):    
        for column in range(0,7):     
            if (((column == 1 or column == 5) and row != 0) 
                or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
                result_str=result_str+"*"    
            else:      
                result_str=result_str+" "    
        result_str=result_str+"\n"    
    print(result_str)
    '''

    n = int(input("Enter the size: "))
    for i in range(n):
        if n == 0:
            print(" "*n+"*")
        elif i == n/2:
            print(" "*(n//2)+"* "*(n//2+1))
        else:
            print(" "*(n-i)+"*"+" "*(2*i-1)+"*")


              

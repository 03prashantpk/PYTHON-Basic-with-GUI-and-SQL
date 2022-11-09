# Day 7 Questions

# Question 1 - CI Calculation
import math
print("\nDay 2 Questions")
print("Available Question No's are 1, 2, 3 and 4 \n")

show_question = int(input("Enter Q.no: "))

# Quetion 1 Starts Here

if show_question == 1:
    '''
    WAP a python function that accepts a string and calculate the number of upper case 
    latter and lower case latters.
    '''

    def upperlower(string):
        upper = 0
        lower = 0

        for i in range(len(string)):

            # For lower letters
            # ord() - converts a character into its Unicode code value.
            if (ord(string[i]) >= 97 and
                    ord(string[i]) <= 122):
                lower += 1

            # For upper letters
            elif (ord(string[i]) >= 65 and
                ord(string[i]) <= 90):
                upper += 1

        print('Lower case characters = %s' % lower,
            '\nUpper case characters = %s' % upper, "\n")

    # Output Code
    string = input("Enter any string here: ")
    upperlower(string)


# Question  2 Starts here


elif show_question == 2:
    '''
    WAP a Python function to check wether a string is pangram or not.
    Note: Pangrams are words or sentences Containing every letter of 
    the alphabates at least once.
    '''

    from string import *

    def checkPangram(s1):
        for c in ascii_lowercase:
            if c not in s1.lower():
                print("It is not Pangram")
                break
            else:
                print("It is a Pangram")

    s = input("Enter a string: ")
    checkPangram(s)


# Quetion 3 Starts Here

elif show_question == 3:
    '''
    WAP a Python program to add "ing" at the end of a given string 
    (length should be at least 3). If the string already ends with "ing"
    then add "EE" instead. If the string length is less than 3 leave it 
    unchanged.
    '''

    string = input("Enter a string: ")
    string2 = "ing"
    string3 = "EE"

    if len(string) >= 3:

        if string2 in string:
            print(string,string3)  # Output with EE
        else:
            print(string,string2) # Output with ing
    else:
        print(string)

# Quetion 4 Starts Here

elif show_question == 4:
    '''
    WAP a puthon program to get string from a given string where all 
    occurences of its first char have been changed to $ expect the frist char itself.

    Example:
    Simple String: 'restart'
    Expected Result: 'resta$t'
    '''
    
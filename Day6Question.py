# Day 6 Questions

# Question 1 - CI Calculation
import math
print("\nDay 2 Questions")
print("Available Question No's are 1 and 2 \n")

show_question = int(input("Enter Q.no: "))

if show_question == 1:
    '''
    Define a function to reverse the digits of an integer.

    Output:
    Enter an integer: 123456
    After Reversal: 54321

    Hint: Devidend = Divisor * Quotient + Reminder
    '''

    def reverse(n):
        while(n > 0):
            digit = n % 10
            n = n//10
            print(digit, end="")
    n = int(input("Enter a Number: "))
    print("After Reversal: ")
    reverse(n)

elif show_question == 2:

    '''
    Write a Python function to check whether a number is perfect or not. 
    ** In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). 
    Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128. 
    '''

    print("\n")

    number = int(input("Enter a number: "))
    num = 0
    for i in range(1, number):
        if(number % i == 0):
            num = num + i
    if (num == number):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

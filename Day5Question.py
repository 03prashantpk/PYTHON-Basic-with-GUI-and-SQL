
# Day 5 Questions

# Question 1 - CI Calculation
print("\nDay 2 Questions")
import math
print("Available Question No's are 1, 2 and 3 \n")

show_question = int(input("Enter Q.no: "))

if show_question == 1:

    ''' WAP a program to calculate the hypo of a rt traiangle taking it 
        perpendicular and base as input.
    '''
    # Import Math
    #import math

    print("\n")
    # taking and assigning perpendcilar and base from user input
    perpendicular = int(input("Enter Perpendicular Length: "))
    base = int(input("Enter base Length: "))

    # Calculating hypo using math function hypot
    hypo = math.hypot(perpendicular, base)

    # print hypotenuse
    print(hypo)
    print("\n")

elif show_question == 2:

    ''' WAP a program basic arithmatic operation by defining functions.
    '''
    print("\n")

    def add_num(a, b):  # function for addition
        sum = a+b
        return sum  # return value

    def sub_num(a, b): 
        sum = a-b
        return sum 

    def mul_num(a, b): 
        sum = a*b
        return sum 

    def div_num(a, b): 
        sum = a/b
        return sum 


    a = int(input("input the number one: "))
    b = int(input("input the number one :"))
    
    # call the function
    print("The sum is", add_num(a, b))
    print("The Substraction is", sub_num(a, b))
    print("The Multiplication is", mul_num(a, b))
    print("The Division is", div_num(a, b))


    print("\n")

elif show_question == 3:
    ''' WAP a program to generate fibonacci series using recursion.
    '''

    print("\n")

    def fibonacci(n):
        if n < 1:
            return n
        
        else: 
            return(fibonacci(n-1)+fibonacci(n-2))
            
            # Dry Run
            # If n = 5;

        
n = int(input("Enter number of term: "))

for i in range(n):
    print(fibonacci(i))
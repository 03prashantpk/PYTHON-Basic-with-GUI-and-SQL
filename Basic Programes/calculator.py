# Break Line
print("\n")
print("\n")

# Input From User
print("Please Enter Integers")
num = int(input("Enter 1st Integer: "))
num1 = int(input("Enter 2st Integer: "))
print("\n")

# Printing Task Detail
print("CHOOSE TASK NUMBER TO EXPLAN TASK")
print("Task No 1 : Addition")
print("Task No 2 : Substraction")
print("Task No 3 : Division")
print("Task No 4 : Multiplication")
print("\n")

# Input User Task Detail
perform = int(input("Enter Task No: "))

if perform == 1:

    # Perform Addition
    print("Addition of", num, "&", num1, "is ", num + num1)
    print("\n")
elif perform == 2:

    # Print Sub
    print("Substraction of", num, "&", num1, "is ", num - num1)
    print("\n")

elif perform == 3:

    # Print Div
    print("Division of", num, "&", num1, "is ", num/num1)
    print("\n")

elif perform == 4:

    # Print Mul
    print("Division of", num, "&", num1, "is ", num*num1)
    print("\n")

else:
    print("Wrong input please try again.")

# Break Line
print("\n")
print("\n")

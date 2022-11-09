# Break Line
print("\n")

# Input From User
num = int(input("Enter a number to check Prime or Not: "))

# Setting For loop (Range)
for number in range(2, num):
    if num % number == 0:
        print(num, "is not Prime")
        break
    else:
        # If (if condition fails ) we will get this message
        print(num, "is Prime")
        break

print("\n")
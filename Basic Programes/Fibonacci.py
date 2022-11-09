# Break Line
print("\n")
print("\n")
print("Fibonacci Series")

n = int(input("Enter a Range: "))
def fibonacci(n):
    a = 0
    b = 1

    if n ==1:
        print(a)
    
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
            if c<=99:
                print(c)
fibonacci(n)


    
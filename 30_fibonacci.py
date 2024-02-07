def fibonacci(n):

    if (n == 0):
        print("the fibonacci is 0")
    elif(n == 1):
        print("the fibonacci is 1")
    elif( n > 0):
        n = (n-1)+(n-2)
        print("the fibonacci is :" ,n)

n = int(input("Enter the number :" ))
print(fibonacci(n))



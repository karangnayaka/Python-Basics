#Simple calaculator
print("simple calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("0. End the program")

while True:
    operation = int(input("Enter Choice(1/2/3/4/0) >>    "))
    num1 = float(input('Enter num1 >>  '))
    num2 = float(input('Enter num2 >>  '))
    if operation==1:
        print(num1+num2)
    elif operation==2:
        print(num1-num2)
    elif operation==3:
        print(num1*num2)
    elif operation==4:
        print(num1/num2)
    else:
        print("Invaliod option! pls ry again")


#functions
def tables(num):

    for i in range(11):
        print(num * i)

def repeat(num):
    for i in range(num):
         print(f"this number made be repeat for {num} times")  #the entered number should be repeated to its times

print("1. Tables \n2. Repeat")
option = int(input("Option>> "))
num = int(input("Enter number>> "))

if option==1:
    tables(num)

elif option==2:
    repeat(num)

else:
    print("ENtered option invalid .try again")



#lcm of two numbers
#lcm = Least common multiple it is the lcm of any two numbers is nothing but the value which is evenly divisible
#by the two given numbers

print("Enter the numbers>> ")
x = int(input("x>> "))
y = int(input("y>> "))

if x>y:
    greater = x

else:
    greater = y

while(True):
    if ((greater%x==0) & (greater%y==0) ):
        lcm = greater
        break
    greater += 1
print(f"lcm of {x} and {y} is {lcm}")













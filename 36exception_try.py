#try
#except
#usage of try and exception in the below program

a = input("enter the number:")
print(f'the Multiplicative table of {a} is ')


try:
   for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a) * i}" )

except:
   print("invalid input")

print("end of the code ")



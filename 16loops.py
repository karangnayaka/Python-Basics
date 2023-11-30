#loops
i = 0
while (i < 10):
    print("hello world")
    i += 1

for i in range(10):
    print("fine")

my_list = [1, 20, 34, 45, 343, 45, 567, 987]

for i in my_list:
    print(i)

good = [2, 2, 2, 6, 6]
for i in good:
    print("*" * i)

resume = ["Karan", 21,"WDC"]
for element in resume:
    print(element)

for num in range(31):
    if num % 7 ==0:
        print(num)
    elif num == 17:
        break
    else:
        continue

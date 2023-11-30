import random

secretnum = random.randint(0,50)
print(secretnum)
count = 1


while(True):
    guess = int(input("Guess the number (0-50) >> "))
    if guess==secretnum:
        print("you guessed it right. Victory!")
        break
    else:
        print("try Again better luck next time")
        count += 1
print(f"You took {count} chances")
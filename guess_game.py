import random

name = input("Enter your name here: ").upper()
num = int(input("Enter your favourate number between (1-100): "))
print(f"Hey, {name} Welcome to Guess,n,Guesses Game😁😁")
print(f"Hope your favourate number ({num}) will bring you happiness ")

low = 1
high = 100
guesses = 0

num = random.randint(low, high) 

while True:
    guess = int(input(f"Enter your guess between ({low}-{high}): "))
    guesses +=1

    if guess > num:
        print(f"{guess} is too high")
    elif guess < num :
        print(f"{guess} is too low")
    else:
        print("You got it right😁‼")
        break

print(f"This round took you {guesses} guesses")
print("=====================================")
print   (f"Here are your Guesses {name}: {guesses}")
print("=====================================")
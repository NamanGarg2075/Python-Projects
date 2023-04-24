import random

max_range = input("Enter maximum range: ")

if max_range.isdigit():
    max_range = int(max_range)
else:
    print("Enter an integer next time")
    quit()

random_number = random.randint(0,max_range)
guess = 0
while True:
    guess+=1    
    guess_number = int(input("Guess a number: "))
    if guess_number > random_number:
        print("You enter a number which is too large")
        continue
    elif guess_number < random_number:
        print("You enter a number which is too small")
        continue
    else:
        print("You got it")
        break

print(f"You takes {guess} attempts to guess the number {random_number}")
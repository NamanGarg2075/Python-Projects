import random

options = ['rock','paper','scissors']

user_win = 0
comp_win = 0

while True:
    user_input = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("INVALID INPUT!!!")
        continue
    random_guess = random.randint(0,2)
    # rock : 0, paper : 1, scissors : 2
    comp_guess = options[random_guess]
    print(f"Computer guessed {comp_guess}")
    if user_input == "rock" and comp_guess == "scissors":
        print("You won!")
        user_win +=1
    elif user_input == "paper" and comp_guess == "rock":
        print("You won!")
        user_win +=1
    elif user_input == "scissors" and comp_guess == "paper":
        print("You won!")
        user_win +=1
    elif user_input == comp_guess:
        print("It's a draw")
    else:
        print("You loss!")
        comp_win +=1

print(f"You won {user_win} times")
print(f"Computer won {comp_win} times")
print("Bye")
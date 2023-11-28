#rock paper scissors Project
#prompt user 1 and user 2 to input either rock paper or scissors
#user 1 (ui)- user 2 import random
#if conditions to determine the winner
import random
choices = ["rock", "paper", "scissors"]
user1 = input('Enter your choice (Rock, Paper or Scissors): ').lower()
if user1 not in choices:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    user1 = input('Enter your choice (Rock, Paper or Scissors): ').lower()
else:
    print('You chose :',user1)

user2 = random.choice(choices)
print('user2 chose: ',user2)

if user1 == user2:
    print("It's a tie!")
elif user1 == "rock" and user2 == "scissors":
    print("Rock smashes scissors! You win")
elif user1 == "paper" and user2 == "rock":
    print("Paper covers rock! You win")
elif user1 == "scissors" and user2 == "paper":
    print("Scissors cuts paper! You win")
else:
    print("user2 wins")
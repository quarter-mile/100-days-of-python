import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option_strings = ["rock", "paper", "scissors"]
options = [rock, paper, scissors]

human_user = input("ROCK, PAPER, SCISSORS?! ")
human_user = human_user.lower()

while human_user not in option_strings:
  human_user = input("You entered something invalid: It's either rock, paper, or scissors! ")
  human_user = human_user.lower()

print("You chose: ")
print(options[option_strings.index(human_user)])
computer_user = option_strings[random.randint(0, 2)]

print("Meanwhile the computer picked: ")
print(options[option_strings.index(computer_user)])

if human_user == "rock" and computer_user == "scissors":
  print("Congratulations! YOU WON!!!")
elif human_user == "paper" and computer_user == "rock":
  print("You win! This just might be your game after all!")
elif human_user == "scissors" and computer_user == "paper":
  print("DING, DING, DING!!! WE HAVE A WINNER!")
elif human_user == computer_user:
  print("Huh... What are the odds? It's a draw.")
else:
  print("Oh well... Better luck next time buddy :(")

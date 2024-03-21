# Rock wins aganist scissors
# scissors wins aganist paper
# Paper wins aganist Rock

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_choice = [rock,paper,scissors]

user_input=int(input("Select\n '0' for Rock\n '1' for Paper\n '2' for scissors\n"))
print(f"{game_choice[user_input]} user_choice")

computer_choice=random.randint(0,2)
print(f"'{computer_choice}' is computer choice")
print(f"{game_choice[computer_choice]} computer_choice")

if computer_choice == user_input:
    print("Draw Match")
elif user_input >=3 or user_input <0:
    print("Invalid User Choice")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose")
elif computer_choice > user_input:
    print("You lose")
elif user_input > computer_choice:
    print("You win!")

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

# Write your code below this line 👇

tool = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number! Try again.")
else:
    print("\nuser chose:\n" + tool[user_choice])
    print("\ncomputer chose:\n" + tool[computer_choice])
    if user_choice == computer_choice:
        print("You draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")

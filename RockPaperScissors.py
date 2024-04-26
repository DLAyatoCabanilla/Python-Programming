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
import random

options = [rock, paper, scissors]
players_choice = int(input("What will you choose? Type '0' for rock, '1' for paper, '2' for scissors: "))
if players_choice >= 3 or players_choice < 0:
    print("You typed an invalid number, You lose.")
else:
    print("You the Player Chose:")
    print(options[players_choice])

    computer_Choice = random.randint(0,2)
    print("Computer chose:")
    print(options[computer_Choice])

    if players_choice == computer_Choice:
        print(players_choice == computer_Choice)
        print("Its a Draw!")
    elif players_choice == 0 and computer_Choice == 2:
        print("Rock Beats Scissors. You WIN!")
    elif players_choice == 2 and computer_Choice == 0:
        print("Rock Beats Scissors. You LOSE!")
    elif players_choice > computer_Choice:
        print("You win!")
    else:
        print("You lose!")



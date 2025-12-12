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

game_list = [rock, scissors, paper]


choice = int(input("Enter your choice:\nType 0 for Rock, 1 for Paper, 2 for Scissors: "))
if choice < 0 or choice >= 3:
    print("\nWrong choice. Play again!")
else:
    print("\nYour choice is: ")

    player_choice = game_list[choice]
    print(player_choice)

    computer_choice = random.choice(game_list)
    print("\nComputer choice is: \n", computer_choice)


    if player_choice == computer_choice:
        print("\nIts a draw!")
    elif player_choice == rock and computer_choice == paper:
        print("\nYou lose!")
    elif player_choice == scissors and computer_choice == rock:
        print("\nYou lose!")
    elif player_choice == paper and computer_choice == scissors:
        print("\nYou lose!")
    else:
        print("\nYou win!")


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
choice = [rock, paper, scissors]
computer_choice = random.choice(choice)
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if human_choice <= 2 and human_choice >= 0:
    print(choice[human_choice])
    print(f"Computer chose: {computer_choice}")
    if choice[human_choice] == computer_choice:
        print("Draw")
    else:
        if human_choice == 0:
            if computer_choice == paper:
                print("You lose!")
            else:
                print("You win!")
        if human_choice == 1:
            if computer_choice == scissors:
                print("You lose!")
            else:
                print("You win!")
        if human_choice == 2:
            if computer_choice == rock:
                print("You lose!")
            else:
                print("You win!")
else:
    print("You entered an invalid number. You lose")


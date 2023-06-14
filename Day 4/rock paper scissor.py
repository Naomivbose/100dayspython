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
user_choice = int(input("What do you chose? put 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
print(f"The computer chose {computer_choice}")
if user_choice >=3 or user_choice < 0:
    print("You put a incorrect number! You lose!")
elif user_choice == 0 and computer_choice == 2: 
    print ("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice:
    print (" it is a draw!")
elif computer_choice > user_choice:
    print ("You lose!")
elif user_choice > computer_choice:
    print ("You win!")




#rock paper scissors game using random module and user input
import random

rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
'''
scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
'''
paper = '''
 _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
'''
comp_choice=random.randint(0,2)
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if comp_choice==0 and user_choice==0:
    print("Computer chose:")
    print(rock)
    print("It's a draw")
elif comp_choice==0 and user_choice==1:
    print("Computer chose:")
    print(rock)
    print("You win!")   
elif comp_choice==0 and user_choice==2:
    
    print("Computer chose:")
    print(rock)
    print("You lose")
elif comp_choice==1 and user_choice==0:
    
    print("Computer chose:")
    print(paper)
    print("You lose")
elif comp_choice==1 and user_choice==1:
    
    print("Computer chose:")
    print(paper)
    print("It's a draw")   
elif comp_choice==1 and user_choice==2:
    
    print("Computer chose:")
    print(paper)
    print("You win!")
elif comp_choice==2 and user_choice==0:
    
    print("Computer chose:")
    print(scissors)
    print("You win!")
elif comp_choice==2 and user_choice==1:
    
    print("Computer chose:")
    print(scissors)
    print("You lose")
elif comp_choice==2 and user_choice==2:
    
    print("Computer chose:")
    print(scissors)
    print("It's a draw")
else:
    print("Invalid input! You lose!")
    
  

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



computers_list= [rock, paper, scissors]
computers_Choice = random.choice(computers_list)

users_Choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n    '))


if users_Choice == 0 and computers_Choice == computers_list[0]:
    print("It's a tie! ")

elif users_Choice == 0 and computers_Choice == computers_list[1]:
    print('You lose! ')

elif users_Choice == 0 and computers_Choice == computers_list[2]:
    print('You win! ')

elif users_Choice == 1 and computers_Choice == computers_list[0]:
    print('You win! ')
elif users_Choice == 1 and computers_Choice == computers_list[1]:
    print("It's a tie! ")
elif users_Choice == 1 and computers_Choice == computers_list[2]:
    print('You lose! ')
elif users_Choice == 2 and computers_Choice == computers_list[0]:
    print('You lose! ')
elif users_Choice == 2 and computers_Choice == computers_list[1]:
    print('You win! ')
elif users_Choice == 2 and computers_Choice == computers_list[2]:
    print("It's a tie! ")

else:
    print('Choose between 0,1, or 2')














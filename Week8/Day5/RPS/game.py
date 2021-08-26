
import random

input("Welcome to Rock, Paper, Scissors! Press anykey to start...")
print()
user_wins = 0
computer_wins = 0

items = ["rock", "paper", "scissors"]

while True:
  random_index = random.randint(0,2)
  AI_choice = items[random_index]

  your_choice = input("Rock, Paper, or Scissors? ").lower()
  while your_choice not in items:
    your_choice = input("That is not a valid item, try again: ").lower()
  
  print()
  print("Your weapon is:", your_choice)
  print("AI weapon is:", AI_choice)
  print()

  if your_choice == 'rock':
    if AI_choice == 'rock':
      print("Seems like It's a tie!")
    elif AI_choice == 'scissors':
      print("You win!")
      user_wins+=1
    elif AI_choice == 'paper':
      print("You lose!")
      computer_wins+=1
  elif your_choice == 'paper':
    if AI_choice == 'paper':
      print("It's a tie!")
    elif AI_choice == 'rock':
      print("You win!")
      user_wins+=1
    elif AI_choice == 'scissors':
      print("You lose!")
      computer_wins+=1
  elif your_choice == 'scissors':
    if AI_choice == 'scissors':
      print("Seems like It's a tie!")
    elif AI_choice == 'paper':
      print("You win!")
      user_wins+=1
    elif AI_choice == 'rock':
      print("You lose!")
      computer_wins+=1

  print()
  print("Now you have "+str(user_wins)+" wins")
  print("The AI has "+str(computer_wins)+" wins")
  print()

  repeat = input("Wanna play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("That is not a valid option, try again: ").lower()
  
  if repeat == 'n':
    print("THANKS FOR PLAYING!")
    break

  print("\n----------------------------\n")
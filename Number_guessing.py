#Number guessing game
from random import randint
best_score = 1000000000


def new_game():
  #The computer chooses a number from 1 to 100
  Number = randint(1, 100)
  global best_score
  if best_score == 1000000000:
    print("There is no best score, it's yours to settle !")
  else:
    print("The current best_score is: " + str(best_score))
  
  #The player tries to guess the number 
  print("Try a number !")
  guess = int(input())
  test = (guess == Number)
  score = 0
  while not test:
    if guess > Number:
      print("My number is lower... Try again !")
      guess = int(input())
    elif guess < Number:
      print("My number is higher... Try again !")
      guess = int(input())
    score += 1
    test = (guess == Number)

    
  print("Congratulations !")
  if score < best_score:
    print("New best score: " + str(score))
    best_score = score
  print("Want to play again ? (Y/N)")
  n = str(input())
  if n == "Y":
    new_game()


new_game()

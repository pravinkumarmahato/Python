import os
import time
import random
board=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board():
    print("-------------- ")
    print("|   |   |   |")
    print('| '+board[1] + ' | ' + board[2] + ' | ' + board[3]+' |')
    print("|   |   |   |")
    print("|---|---|---|")
    print("|   |   |   |")
    print('| '+board[4] + ' | ' + board[5] + ' | ' + board[6]+' |')
    print("|   |   |   |")
    print("|---|---|---|")
    print("|   |   |   |")
    print('| '+board[7] + ' | ' + board[8] + ' | ' + board[9]+' |')
    print("------------- ")

def whoGoesFirst():
  if random.randint(0, 1) == 0:
    return "Player1"
  else:
    return "Player2"

def user_inputX():
  choice = input("Please Choose an empty space for X= ")
  choice=int(choice)
  if board[choice] == " ":
    board[choice]="X"
  else:
    print("Sorry, that space is not empty")

def user_inputO():
  choice = input("Please Choose an empty space for O= ")
  choice=int(choice)
  if board[choice] == " ":
    board[choice]="O"
  else:
    print("Sorry, that space is not empty")
os.system("clear")
whoGoesFirst()

letter =""
while not (letter == "X" or letter == "O"):
  letter = input(whoGoesFirst()+', Do you want to be X or O?')
  letter=letter.upper()
if letter == "X":
  while True:
    os.system("clear")
    display_board()
    user_inputX()
    #winner loop for X
    if (board[1]=='X' and board[2]=='X' and board[3]=='X') or \
    (board[4]=='X' and board[5]=='X' and board[6]=='X') or \
    (board[7]=='X' and board[8]=='X' and board[9]=='X') or \
    (board[1]=='X' and board[4]=='X' and board[7]=='X') or \
    (board[2]=='X' and board[5]=='X' and board[8]=='X') or \
    (board[3]=='X' and board[6]=='X' and board[9]=='X') or \
    (board[1]=='X' and board[5]=='X' and board[9]=='X') or \
    (board[3]=='X' and board[5]=='X' and board[7]=='X'):
      os.system("clear")
      display_board()
      print('Congratulations, X wins!')
      break
    os.system("clear")
    display_board()
    #Check if the match tie
    isFull = True
    if " " in board:
      isFull = False
    if isFull == True:
      print("Tie!")
      break
    user_inputO()
    #winner loop for O
    if (board[1]=='O' and board[2]=='O' and board[3]=='O') or \
    (board[4]=='O' and board[5]=='O' and board[6]=='O') or \
    (board[7]=='O' and board[8]=='O' and board[9]=='O') or \
    (board[1]=='O' and board[4]=='O' and board[7]=='O') or \
    (board[2]=='O' and board[5]=='O' and board[8]=='O') or \
    (board[3]=='O' and board[6]=='O' and board[9]=='O') or \
    (board[1]=='O' and board[5]=='O' and board[9]=='O') or \
    (board[3]=='O' and board[5]=='O' and board[7]=='O'):
      os.system("clear")
      display_board()
      print('Congratulations, O wins!')
      break
    os.system("clear")
    display_board()
    #Check if the match tie
    isFull = True
    if " " in board:
      isFull = False
    if isFull == True:
      print("Tie!")
      break
elif letter == "O":
  while True:
    os.system("clear")
    display_board()
    user_inputO()
    #winner loop for O
    if (board[1]=='O' and board[2]=='O' and board[3]=='O') or \
    (board[4]=='O' and board[5]=='O' and board[6]=='O') or \
    (board[7]=='O' and board[8]=='O' and board[9]=='O') or \
    (board[1]=='O' and board[4]=='O' and board[7]=='O') or \
    (board[2]=='O' and board[5]=='O' and board[8]=='O') or \
    (board[3]=='O' and board[6]=='O' and board[9]=='O') or \
    (board[1]=='O' and board[5]=='O' and board[9]=='O') or \
    (board[3]=='O' and board[5]=='O' and board[7]=='O'):
      os.system("clear")
      display_board()
      print('Congratulations, O wins!')
      break
    os.system("clear")
    display_board()
    #Check if the match tie
    isFull = True
    if " " in board:
      isFull = False
    if isFull == True:
      print("Tie!")
      break
    user_inputX()
    #winner loop for X
    if (board[1]=='X' and board[2]=='X' and board[3]=='X') or \
    (board[4]=='X' and board[5]=='X' and board[6]=='X') or \
    (board[7]=='X' and board[8]=='X' and board[9]=='X') or \
    (board[1]=='X' and board[4]=='X' and board[7]=='X') or \
    (board[2]=='X' and board[5]=='X' and board[8]=='X') or \
    (board[3]=='X' and board[6]=='X' and board[9]=='X') or \
    (board[1]=='X' and board[5]=='X' and board[9]=='X') or \
    (board[3]=='X' and board[5]=='X' and board[7]=='X'):
      os.system("clear")
      display_board()
      print('Congratulations, X wins!')
      break
    os.system("clear")
    display_board()
    #Check if the match tie
    isFull = True
    if " " in board:
      isFull = False
    if isFull == True:
      print("Tie!")
      break
else:
  print("Choose X or O only")

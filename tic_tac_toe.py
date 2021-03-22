import random

flag = True

user_flag = True

board  = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def display_board():
  print(board[0] + '  |  ' + board[1] + '  |  ' + board[2])
  print(board[3] + '  |  ' + board[4] + '  |  ' + board[5])
  print(board[6] + '  |  ' + board[7] + '  |  ' + board[8])


def user_play():
  
  global user_flag
  
  if user_flag:
    position = input('\nChoose a position from 1 to 9: ')
  else:
    position = input('\nThat position is already taken! \nChoose another one: ')
  
  if position.isdigit() and (1<=int(position)<=9):
    
    position = int(position) - 1

    if board[position] == '-':
      board[position] = 'X'
      display_board()
    else:
      user_flag = False
      user_play()
  
  else:
    print('Invalid Entry.')
    user_play()
  


def pc_play():

  available_indexes = []

  for x in range(9):
    if board[x] == '-':
      available_indexes.append(x)
  
  random_index = random.choice(available_indexes)

  board[random_index] = 'O'
  
  print('\nI choose position ' + str(random_index + 1))

  display_board()


def user_win_check():
  
  def user_win():
    global flag
    print('\nCongrats, you won!! :D')
    flag = False
  

  if (board[0] == board[1] == board[2] == 'X' or
      board[3] == board[4] == board[5] == 'X' or
      board[6] == board[7] == board[8] == 'X' or
      board[0] == board[3] == board[6] == 'X' or
      board[1] == board[4] == board[7] == 'X' or
      board[2] == board[5] == board[8] == 'X' or
      board[0] == board[4] == board[8] == 'X' or
      board[2] == board[4] == board[6] == 'X'):

    user_win()
  

def pc_win_check():
  
  def pc_win():
    global flag
    print('\nYou lose, HAHA!! I\'m too smart for you humans...)' )
    flag = False

  if (board[0] == board[1] == board[2] == 'O' or
      board[3] == board[4] == board[5] == 'O' or
      board[6] == board[7] == board[8] == 'O' or
      board[0] == board[3] == board[6] == 'O' or
      board[1] == board[4] == board[7] == 'O' or
      board[2] == board[5] == board[8] == 'O' or
      board[0] == board[4] == board[8] == 'O' or
      board[2] == board[4] == board[6] == 'O'):
      pc_win()


def play_game():
  
  global user_flag
  user_flag = True

  if flag:
    user_play()
  
  user_win_check()
  
  if flag:
    pc_play()
  
  pc_win_check()

  if flag:
    play_game()


want_play = input('\nI dare you to beat me at Tic-Tac-Toe! HEHE... \nWill you face it??  ').lower()
if want_play != 'no':
  print('\nGreat!! Let\'s play!')
  display_board()
  play_game()
elif want_play == 'no':
  print('\nOkay then, joke is on you, bitch!')

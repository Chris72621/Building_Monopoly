import random

BOARD = [[None]] * 11
PLAYERS = []
BANK_CASH = 20580
TOKENS = ['battleship', 'boot', 'cannon', 'horse',  'rider', 'iron', 'racecar', 'dog', 'thimble', 'top' 'hat', 'wheelbarrow']
CHEST = {
    "chance" : {},
    "community" : {}

}


def build_board ():
  # find out how to travel only around the edges
  for i in range(len(BOARD)):
    for j in range(len(BOARD[i])):
      if i == 0 :
        BOARD.append(0)

  print(BOARD)

def throw_dice():
  dice_one = random.randrange(1, 7)
  dice_two = random.randrange(1, 7)
  print(dice_one, dice_two)
  return dice_one

def create_players(name, token):
  PLAYERS.append({
      "name" : name,
      "token" : get_token(token),
      "cash" : bank_withdraw(1500),
      "properties" : []
  })

def get_token(token):
  "Check if player token choice is valid"
  if token.lower() in TOKENS:
    TOKENS.remove(token)
    return token

  print(f'Invalid, choose from list: {TOKENS}')

  token = input('What will you choose?\n')
  return get_token(token)

def bank_withdraw(amount):
  new_bank_cash = BANK_CASH - amount
  return amount

create_players('Christian', 'boot')




print('-----------------------')
print(PLAYERS)
print(TOKENS)


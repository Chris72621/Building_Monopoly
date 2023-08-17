import random

class MonopolyBoardAssembler:
    def __init__(self):
        self.board = [[None]] * 11
        self.players = []
        self.bank_cash = 20580
        self.tokens = ['battleship', 
                      'boot', 'cannon', 
                      'horse',  'rider', 
                      'iron', 'racecar', 
                      'dog', 'thimble', 
                      'top' 'hat', 'wheelbarrow']
        self.chest = {
            "chance" : {},
            "community" : {}
        }

    def build_board (self):
    # find out how to travel only around the edges
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == 0 :
                    self.board.append(0)

  

    def throw_dice(self):
        dice_one = random.randrange(1, 7)
        dice_two = random.randrange(1, 7)
        print(dice_one, dice_two)
        return dice_one

    def create_players(self,name, token):
        self.players.append({
            "name" : name,
            "token" : self.get_token(token),
            "cash" : self.bank_withdraw(1500),
            "properties" : []
        })

    def get_token(self,token):
        "Check if player token choice is valid"
        if token.lower() in self.tokens:
            self.tokens.remove(token)
            return token
        print(f'Invalid, choose from list: {self.tokens}')

        token = input('What will you choose?\n')
        return self.get_token(token)

    def bank_withdraw(self,amount):
        new_bank_cash = self.bank_cash - amount
        return amount

MonopolyBoardAssembler.create_players('Christian', 'boot')

  


import random

class MonopolyBoardAssembler:
    def __init__(self):
        self.board = [[None]] * 11
        self.players = {}
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

    def player_throw_dice(name, self):
        dice_one = random.randrange(1, 7)
        dice_two = random.randrange(1, 7)

        if dice_one == dice_two :
            self.players[name][num_of_roles] += 1

            if self.players[name][num_of_roles] == 1:
                return dice_one + dice_two
            
            if self.players[name][num_of_roles] == 2:
                return dice_one + dice_two
            
            if self.players[name][num_of_roles] == 3:
                a = "jail"
                # Need to come back and put in jail
            
        return dice_one + dice_two
    
    def create_players(self, name, token):
        self.players[name] = {
            "name" : name,
            "token" : self.get_token(token),
            "cash" : self.bank_withdraw(1500),
            "properties" : [],
            "num_of_roles" : 0
        }

        print(self.players)
        print(self.tokens)

    def get_token(self, token):
        "Check if player token choice is valid"
        
        if token.lower() in self.tokens:
            self.tokens.remove(token)
            return token
        
        user_token = input(f'Invalid Token. Avaliable Tokens: {self.tokens}\n')
        return self.get_token(user_token)        
        
        


    def bank_withdraw(self, amount):
        new_bank_cash = self.bank_cash - amount
        return amount

    

# https://www.hasbro.com/common/instruct/00009.pdf

  
a = MonopolyBoardAssembler()
a.create_players('chris','dog')
a.create_players('jesss','cat')

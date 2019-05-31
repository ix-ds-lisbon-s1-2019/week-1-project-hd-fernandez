# Henry Fernandez
# Poker Game

print ('Number of players?')
number_of_players = input()
number_of_players = int(number_of_players)

players = []

for i in range(1, number_of_players + 1):
	print('Enter name of player ('+ str(i) + ')')
	temp_player = input()
	players.append(temp_player)

print('')
print(players)

class Card(object):
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return str(self.rank) + ' of ' + str(self.suit)
    
    VALUE = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A']
    SUIT = ["Hearts","Clubs","Diamonds","Spades"]
    
    def __str__ (self):
        if self.rank == 'J':
            rank = 11
        elif self.rank == 'Q':
            rank = 12
        elif self.rank == 'K':
            rank = 13
        elif self.rank == 'A':
            rank = 14
        else:
            rank = self.rank
           # __repr__(self)
    

#card=Card('Q', 'Diamonds')
#print(card)
deck = []

player_hands = {}

def make_deck():
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        deck.append(card)

make_deck()

def deal_deck():
    for i in players:
        for j in deck:
            player_hands = 
    
        


        
        
        
        


    
    





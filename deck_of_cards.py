import random
from random import shuffle
class Deckofcards():
    def __init__(self):
        self.deck=self.generate()
    def generate(self):
        deck=[]
        suit = ["Hearts","Clubs","Diamonds","Spades"]
        value =["Ace","2","3","4","5","6","7",'8','9','10','Jack','Queen',"King"]
        for count in suit:
            for number in value:
                card=number+" of "+count
                deck.append(card)
        return deck
    def drawCard(self):
        self.shuffle()
        return self.deck.pop()
    # finally the pop will get ride of one card from drawcard


    def shuffle(self):
        shuffle(self.deck)
        return self.deck

class Player():
    def __init__(self,name):
        self.name=name
        self.card=[]
        self.money=10000
    def call(self, num):
        self.money-=num
        return num
    def win(self,num):
        self.money+=num
        return self
    def check(self):
        return self
    def fold(self):
        self.card=[]
        return self
    def getcard(self,card):
        self.card.append(card)
        return self

def game(player1,player2, player3,player4):
    players=[]
    players.append(player1)
    players.append(player2)
    players.append(player3)
    players.append(player4)
    print players
    shuffle(players)
    print players
    deck=Deckofcards()
    money=0
    community_cards=[]
    for indx in range(0,len(players)):
        if indx==0:
            print "PREFLOP ROUND"
            money+=players[0].call(5)
            print players[indx].money
            money+=players[1].call(10)
            print players[indx+1].money
            print money
            for player in players:
                player.getcard(deck.drawCard()).getcard(deck.drawCard())
                print player.card
            print len(deck.deck)

        elif indx==1:
            print "FLOP ROUND"
            for number in range(0,3):
                community_cards.append(deck.drawCard())
            print community_cards
            money+=players[indx].call(5)
            print players[indx].money
            money+=players[indx+1].call(10)
            print players[indx+1].money
            print money
            for person in players:
                for cardofcommunity in community_cards:
                    person.getcard(cardofcommunity)
                print person.card
            print len(deck.deck)
        elif indx==2:
            print "TURN ROUND"
            community_cards.append(deck.drawCard())
            print community_cards
            money+=players[indx].call(5)
            print players[indx].money
            money+=players[indx+1].call(10)
            print players[indx+1].money
            print money
            for gamer in players:
                gamer.getcard(community_cards[3])
                print gamer.card
            print len(deck.deck)
        else:
            print "RIVER ROUND"
            community_cards.append(deck.drawCard())
            print community_cards
            money+=players[indx].call(5)
            print players[indx].money
            money+=players[0].call(10)
            print players[0].money
            print money
            for user in players:
                user.getcard(community_cards[4])
                print user.card
            print len(deck.deck)
            indx =-1
            cards=Deckofcards()
            money=0
BugsySiegel=Player('BugsySiegel')
JackyJohnson=Player('JackyJohnson')
littleDanny=Player('littleDanny')
player=Player('player')
game(BugsySiegel,JackyJohnson,littleDanny,player)
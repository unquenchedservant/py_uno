from game.card import Card
import random

class Deck:
    #going to need an array/list set up for cards
    #array/list for drawPile. Probably can go in init?

    def __init__(self):
        self.cards = []
        self.createDeck()

    def createDeck(self):
        self.addColor("red")
        self.addColor("blue")
        self.addColor("green")
        self.addColor("yellow")
        self.shuffleDeck()
    def addColor(self,color):
        self.cards.append(Card(0, color))
        for i in range(1,12):
            print("hello " + i)
            self.cards.append(Card(i, color))
            self.cards.append(Card(i, color))
        
    def shuffleDeck(self):
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        
    def getLast(self):
        return self.cards[len(self.cards) - 1]
    
    def addCard(self, addedCard):
        self.cards.append(addedCard)

    def printDeck(self):
        for i in range (0, len(self.cards)):
            print(self.cards[i].toString)
    
    def getSize(self):
        return len(self.cards) - 1

    def removeLast(self):
        self.cards.remove(len(self.cards) - 1)

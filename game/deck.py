class Deck:
    #going to need an array/list set up for cards
    #array/list for drawPile. Probably can go in init?

    def __init__(self):
        #initialize cards
        #add cards. This is going to be a lot of fun. 
        #red, blue, green, yellow cards. 1 0, 2 of every other except card 13 and 14
        pass 
    
    def shuffleDeck(self):
        pass
        #look up python shuffle library similar to Collections.shuffle(cards)
        #do this twice
        
    def getLast(self):
        pass
        #return cards.get(cards.size()-1) but in python
    
    def addCard(self, addedCard):
        self.add(addedCard)

    def printDeck():
        pass
        #this is where we will figure out how to display the cards on to the curses screen
    
        ###
        # java: 
        # for(int i = 0; i < cards.size; i++){
        #   Card sd = new Card(cards.get(i).getCardNumber, cards.get(i).getCardColor());
        #   System.out.println(sd.toString())
        # }
    
    def getSize():
        pass
        #JAVA return cards.size();

    def removeLast():
        pass
        #JAVA cards.remove(cards.size()-1)

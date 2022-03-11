class Deal: # why is this deal and not hand?

    def __init__(self):
        self.hand = []

    def addCardFromDeck(self, deck):
        self.hand.append(deck.getLastCard())
        deck.removeLastCard()

    def addCard(self, addCard):
        self.hand.append(addCard)

    def removeCard(self,elem):
        self.hand.remove(elem)
    
    def getCard(self, elem):
        return self.hand.get(elem)

    ''' def getSize():
        pass
        #returns hand.size(); (size is provided by the ArrayList library)
    '''

    '''def printArray():
        pass
        #I recall hating this method name as well
        #Java : System.out.println(hand.toString()); (hand.toString() is provided by the 
        # card object)
    '''
    '''
    def getLast():
        pass
        #return hand.get(hand.size()-1) 
        #not really sure why this couldn't just be utilized with the getCard function. 

    

    '''
    
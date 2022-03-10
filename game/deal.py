class Deal:
    #java adds private ArrayList<Card> hand;
    #i believe the point of this it to establish a hand for the dealer. 
    #If I remember correctly, this is a poorly titled class name that I may change later.
    def __init__(self):
        pass
        # hand = new Arraylist<>();

    def addCard(deck):
        #these are overloaded
        #this one in Java
        #
        # hand.add(deck.getLast())
        # deck.removeLast()
        
        # This is for when a player needs to draw a new card
    
        pass
    def addCard(addCard):
        pass
        #see above. 
        #JAVA is hand.add(addCard)
        #
        #I suppose this is when you want to add a specific card. 

    def removeCard(elem):
        pass
        #when you need to a remove a card from a player's hand, typically in playing the card. 
        #JAVA hand.remove(elem) (remove is provided by the ArrayList library)    
    def getCard(elem):
        pass
        #returns hand.get(elem)
        #This is when you just want to get the card without doing anything to it
    
    def getSize():
        pass
        #returns hand.size(); (size is provided by the ArrayList library)
    
    def printArray():
        pass
        #I recall hating this method name as well
        #Java : System.out.println(hand.toString()); (hand.toString() is provided by the 
        # card object)

    def getLast():
        pass
        #return hand.get(hand.size()-1)
        #not really sure why this couldn't just be utilized with the getCard function. 

    

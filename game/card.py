class Card:
    def __init__(self, number, color):
        self.cardNumber = number
        self.cardColor  = color
    
    def getCardNumber(self):
        return self.cardNumber
    def getCardColor(self):
        return self.cardColor
    #def getCardColor(card): This is copied over from my original uno game written in java. I don't think it's necessary though
    #    return card.getCardColor()
    def toString(self):
        color = None
        number = None
        if self.cardColor == "r":
            color = "Red"
        elif self.cardColor == "b":
            color = "Blue"
        elif self.cardColor == "g":
            color = "Green"
        elif self.cardColor == "y":
            color = "Yellow"
        elif self.cardColor == "a":
            color = "Any"
        if self.cardNumber <= 9:
            number = str(self.cardNumber)
        elif self.cardNumber == 10:
            number = "Skip"
        elif self.cardNumber == 11:
            number = "Draw Two"
        elif self.cardNumber == 12:
            number = "Reverse"
        elif self.cardNumber == 13:
            number = "Wild"
        elif self.cardNumber == 14:
            number = "Wild Draw Four"
        return color + " - " + number


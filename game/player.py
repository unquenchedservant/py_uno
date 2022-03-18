from game.deal import Deal


class Player:
    # start of new class for Player
    # This should keep code redundancy down.
    def __init__(self,isPlayer=False):
        self.isPlayer = isPlayer
        self.hand = Deal().hand
        self.score = 0
        self.name = ""



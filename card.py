class Card:
    def __init__(self, rank, suit, sortValue):
        self._rank = rank
        self._suit = suit
        self._idOnHand = None
        self._cardOfJoker = None
        self._nameTable = {
            "zeleny": "Z",
            "cerveny": "C",
            "zaludy": "Za",
            "kule": "K",
            "zolik": "Zo"
            


        }

        self.valueTable = {
            "J":11,
            "Q":12,
            "K":13,
            "A":14,
            "Z":15,
        }

        self.sortValue = sortValue

    def __repr__(self):
        return f"{self._nameTable[self._suit]}{self._rank}"
    
    @property
    def rank(self):
        if type(self._rank) == int:
            return self._rank
        else:
            return self.valueTable[self._rank]
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def idOnHand(self):
        return self._idOnHand
    
    @property
    def value(self):
        if self._rank == "A":
            return 10
        elif self._rank in ["J", "Q", "K", "Z"]:
            return 10
        else:
            return int(self._rank)
    
    @property
    def cardOfJoker(self):
        return self._cardOfJoker
    

    @cardOfJoker.setter
    def cardOfJoker(self, card):
        self._cardOfJoker = card


    @idOnHand.setter
    def idOnHand(self, id):
        self._idOnHand = id




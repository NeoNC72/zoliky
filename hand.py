import card

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards : list[card.Card] = []
        self.cardIds = []
        self.currentId = 0
    
    def add_card(self, card:card.Card):
        self.cards.append(card)
        self.cardIds.append(self.currentId)
        card.idOnHand = self.currentId
        self.currentId += 1
        self.sort_hand()
    
    def remove_card(self, id):
        for i in range(len(self.cards)):
            if self.cardIds[i] == id:
                tmp = self.cards.pop(i)
                self.cardIds.pop(i)
                return tmp
        self.sort_hand()
    
    def return_card(self, id):
        for i in range(len(self.cards)):
            if self.cardIds[i] == id:
                return self.cards[i]
        self.sort_hand()
                
    @property
    def value(self):
        ret = 0
        for card in self.cards:
            ret += card.value
        return ret

    def sort_hand(self):
        self.cards.sort(key=lambda x: x.sortValue)

    def give_cardIds(self):
        return self.cardIds

    def possible_combos(self):
        combos = []
        cardindex = 0
        cindex = 0
        while cardindex < len(self.cards):
            startlen = len(combos)
            if cardindex == len(self.cards) - 1:
                break
            while True:
                if cardindex >= len(self.cards) - 1:
                    break
                if self.cards[cardindex].rank == self.cards[cardindex + 1].rank - 1 and self.cards[cardindex].suit == self.cards[cardindex + 1].suit:
                    combos.append([])
                    if combos[cindex] == []:
                        combos[cindex].append(self.cards[cardindex])
                    combos[cindex].append(self.cards[cardindex + 1])
                    if cardindex == len(self.cards) - 1:
                        break
                    cardindex += 1
                elif self.cards[cardindex].rank == self.cards[cardindex + 1].rank and self.cards[cardindex].suit == self.cards[cardindex + 1].suit:
                    cardindex += 1
                else:
                    break
            
            if len(combos) == startlen:
                cardindex += 1
            else:
                cindex += 1
        if len(combos) != 0:
            ret = []
            for combo in combos:
                if len(combo) > 2:
                    ret.append(combo)

            
        return ret
            

    


    def __repr__(self):
        ret = ""
        for card in range(len(self.cards)):
            ret += f"{self.cards[card]}({self.cardIds[card]}) "


        return f"{self.name}: {ret} Value: {self.value}"
import card
import json
import random

class Deck:
    def __init__(self, type):
        deckData = json.load(open("deck.json"))
        self.cards = []
        i = 0
        if type == "full":
            for _ in range(2):
                for suit in deckData:
                    for rank in deckData[suit]:
                        self.cards.append(card.Card(rank, suit, i))
                        i += 1
                i = 0
                
        
    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        return self.cards.pop()
    
    def add_card(self, card:card.Card):
        self.cards.append(card)
    
    def card_on_top(self):
        return self.cards[-1]

    def __repr__(self):
        return f"{self.cards} Deck size: {len(self.cards)}\n"
    
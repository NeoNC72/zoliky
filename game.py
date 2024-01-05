import card
import table
import random
class Game:
    def __init__(self, players, AIs, deck, tabledeck, autoplay = False, autoplaytoturn = 3):
        self.players = players
        self.AIs = AIs
        self.deck = deck
        self.tabledeck = tabledeck
        self.table = table.Table(players)
        self.turn = 0
        self.subturn = 0
        self.playercount = len(players)
        self.onTurn = 0
        self.autoplay = autoplay
        self.autoplaytoturn = autoplaytoturn
    
    def deal(self):
        fixed = [card.Card(2, "zeleny", 0), card.Card(3, "zeleny", 1), card.Card(4, "zeleny", 2), card.Card(4, "zeleny", 2), card.Card(5, "zeleny", 3), card.Card(6, "zeleny", 4)]
        for _ in range(7):
            for player in self.players:
                if player.name == "FIXED":
                    if len(fixed) != 0:
                        player.add_card(fixed.pop())
                        player.add_card(fixed.pop())
                else:    
                    player.add_card(self.deck.take_card())
                    player.add_card(self.deck.take_card())
        
        #self.players[0].add_card(self.deck.take_card())

    def play(self):
        while True:
            currPlayer = self.players[self.onTurn]
            print(f"Turn: {self.turn} Subturn: {self.subturn}")
            print(f"table: {self.table}")
            if self.onTurn in self.AIs:
                pass
            else:
                play = ""
                if len(self.tabledeck.cards) != 0:
                    print(f"Card on top: {self.tabledeck.card_on_top()}")
                while play != "q":
                    if self.autoplay and self.turn < self.autoplaytoturn:
                        play = "s"
                    else:
                        play = input("Play: ")

                    if play == "s":
                        if currPlayer.name != "FIXED":
                            card = self.deck.take_card()
                            currPlayer.add_card(card)
                            print(f"You took {card}\n")
                        print(currPlayer)
                        print(currPlayer.possible_combos())
                        if self.turn > 2:
                            inp = input("Put on table: ")
                            if inp == "y":

                                inp = input("Card id to put on table: ")
                                while inp != "s":
                                    toput = []
                                    self.tabledeck.add_card(currPlayer.remove_card(int(inp)))
                                    print(currPlayer)
                                    inp = input("Card id to add card to flush (s do): ")
                                    toput.append(currPlayer.return_card(int(inp)))
                                    if self.valid_flush(toput):
                                        for card in toput:
                                            self.table.put_out(currPlayer, card)
                                        print(currPlayer)
                                        break
                        if self.autoplay and self.turn < self.autoplaytoturn:
                            self.tabledeck.add_card(currPlayer.remove_card(random.choice(currPlayer.give_cardIds)))
                        else:
                            self.tabledeck.add_card(currPlayer.remove_card(int(input("Card id to throw: "))))
                        print(currPlayer)
                        
                        
                        self.subturn += 1
                        if self.subturn == self.playercount:
                            self.turn += 1
                            self.subturn = 0
                            self.onTurn = 0
                        else:
                            self.onTurn += 1
                        break
                            
                    elif play == "p":
                        print(currPlayer)
                    
                    elif play == "t":
                        print(self.table)
                    
    
            
    def valid_flush(self, cards):
        if len(cards) < 3:
            return False
        for i in range(len(cards) - 1):
            if cards[i].rank != cards[i + 1].rank - 1 or cards[i].suit != cards[i + 1].suit:
                return False
        return True


    def __repr__(self):
        ret = f"Table:\n{self.tabledeck}\n"
        ret += f"Deck:\n{self.deck}\n"
        for player in self.players:
            ret += f"{player}\n"
        return ret
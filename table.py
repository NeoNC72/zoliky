import hand

class Table:
    def __init__(self, players) -> None:
        self.cards_out = {}

        for player in players:
            player : hand.Hand
            self.cards_out[player.name] = []    

    def put_out(self, player:hand.Hand, cards):
        self.cards_out[player.name].append(cards)

    def __repr__(self):
        ret = ""
        for player in self.cards_out:
            ret += f"{player} cards: {self.cards_out[player]}\n"
        return ret
import card
import deck
import hand
import game

deck1 = deck.Deck("full")
deck1.shuffle()
tabledeck = deck.Deck("empty")



player1 = hand.Hand("FIXED")
player2 = hand.Hand("AI1")
player3 = hand.Hand("AI2")
player4 = hand.Hand("AI3")


game = game.Game([player1, player2, player3, player4], [], deck1, tabledeck,True, 3)

game.deal()

game.play()

print(game)
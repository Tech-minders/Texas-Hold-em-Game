from card import Card
import random

class Deck():

    def __init__(self):
        # Note: Ensure Card.RANKS and Card.SUITES are defined in your Card class
        ranks = Card.RANKS
        suites = Card.SUITES
        deck = [] 

        for rank in ranks:
            for suite in suites:
                card = Card(suite=suite, rank=rank)
                deck.append(card)
        self.deck = deck

    def shuffle(self):
        newDeck = []
        # Use list() to create a copy so you don't empty self.deck permanently during the loop
        temp_deck = list(self.deck) 
        
        while len(temp_deck) > 0:
            n = random.randint(0, len(temp_deck) - 1)
            card = temp_deck.pop(n) # Correctly removes and returns the item
            newDeck.append(card)

        print("new Deck length", len(newDeck))
        self.deck = newDeck
        
        for card in self.deck:
            card.printCard()
            print("---")

    def burn_card(self):
        # Takes top card (index 0) and moves it to the bottom (end of list)
        if self.deck:
            top_card = self.deck.pop(0)
            self.deck.append(top_card)

    def give_card(self):
        # Removes and returns the last card in the deck
        if self.deck:
            return self.deck.pop()
        return None

if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()

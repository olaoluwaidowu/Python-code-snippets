"""
   Author: Olaoluwa Idowu
   Student ID: 0372483
   Assignment No: 6
   Title: Deck of Cards
   Date: 4-02-2022  
"""


# importing Card class from card.py
from card import Card

# class to store and display the list of cards
class Deck:

    # method to initialise objects 
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)
        
        
    # method to add 52 cards to the deck    
    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        cards = []
        #self._cards = [Card(s, n) for s in suits for n in numbers]
        for suit in suits:
            for number in numbers:
                cards.append(Card(suit, number))

        self._cards = cards


# An instance of Deck
deck_of_cards = Deck()

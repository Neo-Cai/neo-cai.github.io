# Author: Neo Cai
# Date: 02/8/22
# File Name: card.py
# Course: Computer Science 1
# Purpose: Card class creates a card with corresponding numbers and suits

class Card:
    # Constructor initializes the number and suit of the card
    def __init__(self, number, suit):
        self.number_int = number
        self.suit_int = suit

    # Method that sorts the suit value into a suit name instead
    def suit(self):
        if self.suit_int == 1:
            return "clubs"
        elif self.suit_int == 2:
            return "spades"
        elif self.suit_int == 3:
            return "diamonds"
        elif self.suit_int == 4:
            return "hearts"

    # Method that sorts the card number to card name instead, so 1 = Ace, 13 = King
    def value(self):
        if 11 <= self.number_int <= 13:
            if self.number_int == 11:
                return "Jack"
            elif self.number_int == 12:
                return "Queen"
            elif self.number_int == 13:
                return "King"
        elif self.number_int == 1:
            return "Ace"
        else:
            return str(self.number_int)

    # Method that returns the string name of the card, concatenates the value and suit
    def __str__(self):
        return self.value() + " of " + self.suit()





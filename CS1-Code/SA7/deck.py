# Author: Neo Cai
# Date: 02/8/22
# File Name: deck.py
# Course: Computer Science 1
# Purpose: Create a deck of cards from the card class and some functions to play with the deck

from card import Card
from random import randint


class Deck:
    # Constructor that initializes a card list
    def __init__(self):
        self.card_list = []

    # Method creates a deck of cards (52 cards because there are no jokers)
    def add_standard_cards(self):
        for i in range(1, 5):  # nested loop starts going through every suit
            for j in range(1, 14):  # then adds numbers for each suit
                self.card_list.append(Card(j, i))  # appends the suit-number pair

    # Method shuffles the deck by taking an indexed card and swapping it with another random card
    def shuffle(self):
        for i in range(len(self.card_list)):
            rand_index = randint(0, len(self.card_list) - 1)
            temp = self.card_list[i]  # stores indexed card
            self.card_list[i] = self.card_list[rand_index]  # assigns indexed card with random card
            self.card_list[rand_index] = temp  # completes the swap

    # Method takes the last card of the deck and stores it, then deletes the last index of the deck
    def pop(self):
        indexed_card = self.card_list[len(self.card_list) - 1]  # stores card
        del self.card_list[len(self.card_list) - 1]  # deletes index
        return indexed_card  # returns it for use in deal method

    # Method deals a hand of a given size
    def deal(self, number):
        hand = Deck() # creates a new deck
        for i in range(number):
            hand.card_list.append(self.pop())  # adds the indexed card (last card in deck) to hand
        return hand  # returns hand to be used



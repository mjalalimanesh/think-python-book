"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        ts = sorted(self.cards, key=lambda x: x.rank)
        for i in range(len(ts) - 1):
            if ts[i].rank == ts[i + 1].rank:
                return True
        return False

    def has_twopair(self):
        ts = sorted(self.cards, key=lambda x: x.rank)
        count = 0
        i = 0
        while i < (len(ts) - 1):
            if ts[i].rank == ts[i + 1].rank:
                count = count + 1
                if count >= 2:
                    return True
                i = i + 2
                continue
            i = i + 1
        return False

    def classify(self):
        if self.has_flush():
            self.label = "flush"
            return
        if self.has_twopair():
            self.label = "two-pair"
            return
        if self.has_pair():
            self.label = "pair"
            return


def table_of_classification(number_of_hands):
    d = {}
    for i in range(number_of_hands):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.classify()
        d[hand.label] = d.get(hand.label, 0) + 1
    return d


if __name__ == "__main__":
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_twopair())
        print("")

    deck = Deck()
    d = table_of_classification(1000)
    print(d)

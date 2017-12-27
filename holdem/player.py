from . import exceptions

class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards = []
        self._chip_count = 0

    def deal_hole_card(self, card):
        """Deal a hole card to the player"""
        if len(self._cards) >= 2:
            raise exceptions.TooManyCardsException
        self._cards.append(card)

    def collect_hole_cards(self):
        """Return the hole cards and clear this player's cards."""
        hole_cards = self._cards
        self._cards = []
        return hole_cards

    def award_chips(self, chips):
        self._chip_count += chips

    @property
    def name(self):
        return self._name

    @property
    def chip_count(self):
        return self._chip_count


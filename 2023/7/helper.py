from enum import Enum
import copy

class Cards(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 1 # in first part its 11, in second its 1
    QUEEN = 12
    KING = 13
    ACE = 14

class HandStrength(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

def return_enum_value(card):
    if card == '2':
        return Cards.TWO
    if card == '3':
        return Cards.THREE
    if card == '4':
        return Cards.FOUR
    if card == '5':
        return Cards.FIVE
    if card == '6':
        return Cards.SIX
    if card == '7':
        return Cards.SEVEN
    if card == '8':
        return Cards.EIGHT
    if card == '9':
        return Cards.NINE
    if card == 'T':
        return Cards.TEN
    if card == 'J':
        return Cards.JACK
    if card == 'Q':
        return Cards.QUEEN
    if card == 'K':
        return Cards.KING
    if card == 'A':
        return Cards.ACE
    return -1

class Hand:
    def __init__(self, hand, bid):
        self.card_values = []
        number_of_jokers = 0
        for char in hand:
            if char == 'J':
                number_of_jokers += 1
            self.card_values.append(return_enum_value(char))

        temp_dict = {}
        for card in self.card_values:
            if card in temp_dict:
                temp_dict[card] += 1
            else:
                temp_dict[card] = 1

        strongest_group = 1
        second_strongest_group = 1
        for card_value in temp_dict.keys():
            if temp_dict[card_value] > strongest_group and temp_dict[card_value] > second_strongest_group:
                second_strongest_group = strongest_group
                strongest_group = temp_dict[card_value]
                continue
            if temp_dict[card_value] > second_strongest_group:
                second_strongest_group = temp_dict[card_value]

        if strongest_group == 1:
            if number_of_jokers == 1:
                # if one of those high cards is jack, that means we can produce 1 pair
                self.hand_strength = HandStrength.ONE_PAIR
            else:
                self.hand_strength = HandStrength.HIGH_CARD
        if strongest_group == 2 and second_strongest_group == 1:
            if number_of_jokers == 2 or number_of_jokers == 1:
                # it means jokers are the first, group, and when grouped with one of the rest cast, you get three of a kind
                self.hand_strength = HandStrength.THREE_OF_A_KIND
            else:
                self.hand_strength = HandStrength.ONE_PAIR
        if strongest_group == 2 and second_strongest_group == 2:
            if number_of_jokers == 2:
                self.hand_strength = HandStrength.FOUR_OF_A_KIND
            elif number_of_jokers == 1:
                self.hand_strength = HandStrength.FULL_HOUSE
            else:
                self.hand_strength = HandStrength.TWO_PAIR
        if strongest_group == 3 and second_strongest_group == 1:
            if number_of_jokers == 3 or number_of_jokers == 1:
                self.hand_strength = HandStrength.FOUR_OF_A_KIND
            else:
                self.hand_strength = HandStrength.THREE_OF_A_KIND
        if strongest_group == 3 and second_strongest_group == 2:
            if number_of_jokers == 3 or number_of_jokers == 2:
                self.hand_strength = HandStrength.FIVE_OF_A_KIND
            else:
                self.hand_strength = HandStrength.FULL_HOUSE
        if strongest_group == 4:
            if number_of_jokers == 4 or number_of_jokers == 1:
                self.hand_strength = HandStrength.FIVE_OF_A_KIND
            else:
                self.hand_strength = HandStrength.FOUR_OF_A_KIND
        if strongest_group == 5:
            self.hand_strength = HandStrength.FIVE_OF_A_KIND

        self.bid = int(bid.strip())

    def is_bigger_than(self, hand):
        if self.hand_strength.value > hand.hand_strength.value:
            return True
        elif self.hand_strength.value < hand.hand_strength.value:
            return False
        for i in range(5):
            if self.card_values[i].value > hand.card_values[i].value:
                return True
            elif self.card_values[i].value < hand.card_values[i].value:
                return False
        return -1   # this means they are same

    def is_bigger_than_whole_list_of_cards(self, list_of_hands):
        for hand in list_of_hands:
            if hand.is_bigger_than(self):
                return False
        return True

def find_best_hand_in_list(list_of_hands):
    for i in range(len(list_of_hands)):
        temp_list = copy.deepcopy(list_of_hands)
        test_max_hand = temp_list.pop(i)
        if test_max_hand.is_bigger_than_whole_list_of_cards(temp_list):
            return list_of_hands[i]



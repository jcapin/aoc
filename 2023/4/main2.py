import re


# class Card:
#     def __init__(self, card_number, winning_numbers, my_numbers):
#         self.card_number = card_number
#         self.winning_numbers = winning_numbers
#         self.my_numbers = my_numbers
#         winning_out_of_my_numbers = []
#         for my_num in my_numbers:
#             if my_num in winning_numbers:
#                 winning_out_of_my_numbers.append(my_num)
#         self.winning_out_of_my_numbers = winning_out_of_my_numbers
#
#     def print(self):
#         print(str(self.card_number) + ' -> ' + str(len(self.winning_out_of_my_numbers)))
#

def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    total_sum_of_scratch_cards = 0

    map_of_cards = {}

    for i in range(len(lines)):
        current_line = lines[i]

        card_no_str = re.search('[0-9]+', current_line).group().strip()
        card_no = int(card_no_str)

        winning_numbers_string = current_line[current_line.find(':') + 2:].split('|')[0].strip()
        my_numbers_string = current_line[current_line.find(':') + 2:].split('|')[1].strip()

        winning_numbers = winning_numbers_string.split(' ')
        my_numbers = my_numbers_string.split(' ')

        for element in winning_numbers:
            if element.strip() == '':
                winning_numbers.remove(element)

        for element in my_numbers:
            if element.strip() == '':
                my_numbers.remove(element)

        winning_out_of_my_numbers = []
        for my_num in my_numbers:
            if my_num in winning_numbers:
                winning_out_of_my_numbers.append(my_num)
        # fill with starting cards
        map_of_cards[card_no] = len(winning_out_of_my_numbers)

    map_of_number_of_cards = {}

    for card_number in map_of_cards.keys():
        map_of_number_of_cards[card_number] = 1
        # print(str(card_number)+' -> '+str(map_of_cards[card_number]))
    #
    # for card_number in map_of_number_of_cards.keys():
    #     print(str(card_number)+' ===> '+str(map_of_number_of_cards[card_number]))

    for card_number in map_of_number_of_cards.keys():
        for win in range(map_of_number_of_cards[card_number]):
            for next_card_number in range(card_number+1,card_number+1+map_of_cards[card_number]):
                map_of_number_of_cards[next_card_number] += 1
                # print(f'Card {card_number} has {map_of_cards[card_number]} winning numbers, therefore I get card {
                # next_card_number}')

    # for card_number in map_of_number_of_cards.keys():
    #     print(str(card_number)+' ===> '+str(map_of_number_of_cards[card_number]))

    for card_no in map_of_number_of_cards.keys():
        total_sum_of_scratch_cards += map_of_number_of_cards[card_no]

    return total_sum_of_scratch_cards


if __name__ == '__main__':
    print(solution())

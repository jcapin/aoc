import re
import helper


def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    hand_list = []
    for line in lines:
        cards = line.split(' ')[0]
        bid = line.split(' ')[1]
        new_card = helper.Hand(cards, bid)
        hand_list.append(new_card)

    map_with_same_strengths = {}

    for hand in hand_list:
        if hand.hand_strength in map_with_same_strengths:
            map_with_same_strengths[hand.hand_strength].append(hand)
        else:
            map_with_same_strengths[hand.hand_strength] = [ hand ]

    print(map_with_same_strengths)

    iterating_strengths = [helper.HandStrength.FIVE_OF_A_KIND, helper.HandStrength.FOUR_OF_A_KIND,
                           helper.HandStrength.FULL_HOUSE, helper.HandStrength.THREE_OF_A_KIND,
                           helper.HandStrength.TWO_PAIR, helper.HandStrength.ONE_PAIR,
                           helper.HandStrength.HIGH_CARD]

    winning_order = []

    for i in iterating_strengths:
        if i not in map_with_same_strengths.keys():
            continue
        while map_with_same_strengths[i] != []:
            if len(map_with_same_strengths[i]) == 1:
                winning_order.append(map_with_same_strengths[i][0])
                map_with_same_strengths[i].pop(0)
                break
            next_strongest_hand = helper.find_best_hand_in_list(map_with_same_strengths[i])
            winning_order.append(next_strongest_hand)
            map_with_same_strengths[i].remove(next_strongest_hand)

    print(winning_order)

    total_sum = 0
    for i in range(len(winning_order)):
        total_sum += winning_order[i].bid * (len(winning_order)-i)

    print(total_sum)


    return 0


if __name__ == '__main__':
    print(solution())

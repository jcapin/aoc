import re
def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    total_sum = 0

    for i in range(len(lines)):
        current_line = lines[i]

        winning_numbers_string = current_line[current_line.find(':')+2:].split('|')[0].strip()
        my_numbers_string = current_line[current_line.find(':')+2:].split('|')[1].strip()

        winning_numbers = winning_numbers_string.split(' ')
        my_numbers = my_numbers_string.split(' ')

        for element in winning_numbers:
            if element.strip() == '':
                winning_numbers.remove(element)

        for element in my_numbers:
            if element.strip() == '':
                my_numbers.remove(element)

        # print(winning_numbers)
        # print(my_numbers)

        winning_out_of_my_numbers = []
        for my_num in my_numbers:
            if my_num in winning_numbers:
                winning_out_of_my_numbers.append(my_num)

        if len(winning_out_of_my_numbers) > 0:
            total_sum += pow(2, len(winning_out_of_my_numbers)-1)
    return total_sum


if __name__ == '__main__':
    print(solution())

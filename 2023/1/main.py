def solution():
    number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    with open('data') as file:
        lines = [line.strip() for line in file]

    total_sum = 0
    for line in lines:
        num = ''
        i = 0
        while i < len(line):
            if line[i].isdigit():
                num += line[i]
                i += 1
            else:
                for key in number_dict.keys():
                    if line.startswith(key, i):
                        num += str(number_dict[key])
                        i += len(key) - 1
                        break
                else:
                    num += line[i]
                    i += 1
        num = ''.join(char for char in num if char.isdigit())

        total_sum += int(num[0] + num[-1])

    return total_sum


if __name__ == '__main__':
    print(solution())

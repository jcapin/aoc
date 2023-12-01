def solution():
    dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    standardized_data = []
    non_standardized_data = []
    with open('data') as file:
        for line in file:
            non_standardized_data.append(line.strip())
            before_iter_line = ''  # part of string which was already examined and standardized
            iter_line = line.strip()
            while True:
                if not iter_line:  # we have examined everything that is to be examined
                    break
                if iter_line[0].isdigit():  # just copy digit as it is and go to next char
                    before_iter_line += iter_line[0]
                    iter_line = iter_line[1:]
                    continue
                key_found = False
                for key in dict.keys():  # iterating through number as words
                    if iter_line.startswith(key):  # line from iterator onwards starts with any of the number words
                        before_iter_line += str(dict.get(key))
                        iter_line = iter_line[len(key) - 1:]  # instead of word put actual number
                        # "oneight" should be 18, therefore replace "one" with "1e" so next number can take it too
                        key_found = True
                        break
                if not key_found:
                    if iter_line:  # Check if iter_line is not empty
                        before_iter_line += iter_line[0]    # char not part of number, just skip through it
                        iter_line = iter_line[1:]
            standardized_data.append(before_iter_line.strip())
    sum = 0
    # print(standardized_data)    # all number words in lines replaced, data ready for calculation
    for i in range(len(standardized_data)):
        num = ''
        for char in standardized_data[i]:
            if (char.isdigit()):    # add all digits into a string of numbers
                num += char
        # print(non_standardized_data[i]+' === '+standardized_data[i]+' ---> '+num+' === '+num[0]+num[-1])
        sum += int(num[0] + num[-1])    # increase sum by first and last digit from each line
    return sum


if __name__ == '__main__':
    print(solution())

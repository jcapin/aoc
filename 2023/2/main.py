import re
def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    diction = {'red': 12, 'green': 13, 'blue': 14}
    total_sum = 0   # sum of indexes for first part of the task

    total_sum_second = 0    # sum of multiplications for the second part of the task

    for game in lines:
        temp_string = game[5:]
        game_index = re.search('[0-9]+', temp_string).group().strip()

        temp_string = temp_string[len(game_index)+2:]    # skip number and ": "

        limit_surpassed = False

        enough_balls_dict = {'red': 0, 'green': 0, 'blue': 0}

        for outcome in temp_string.split(';'):
            for balls_set in outcome.strip().split(','):
                no_of_balls_str = re.search('[0-9]+', balls_set.strip()).group().strip()
                no_of_balls = int(no_of_balls_str)

                color = balls_set[len(no_of_balls_str) + 1:].strip()

                if no_of_balls > enough_balls_dict.get(color):
                    enough_balls_dict[color] = no_of_balls

                if no_of_balls > diction.get(color):
                    limit_surpassed = True

        tmp_multi = 1

        for color in enough_balls_dict.keys():
            tmp_multi *= enough_balls_dict.get(color)

        total_sum_second += tmp_multi

        if not limit_surpassed:
            total_sum += int(str(game_index))

    return total_sum_second     # return total_sum for first part of task


if __name__ == '__main__':
    print(solution())

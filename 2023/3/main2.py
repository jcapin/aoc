import re
def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    #{ i: {j: [firstNum, secondNum]}  }

    # [i, j]
    total_gear_sum = 0
    total_sum = 0
    gears = []

    for i in range(len(lines)):
        current_line = lines[i]

        skip_no = 0

        for j in range(len(current_line)):
            if skip_no > 0:
                skip_no = skip_no - 1
                continue
            next_num_str = re.search('[0-9]+', current_line[j:])
            if not next_num_str:
                continue
            next_num_str = next_num_str.group().strip()

            if next_num_str:

                if current_line.find(next_num_str) == 0:
                    start_index = 0
                else :
                    start_index = j + current_line[j:].find(next_num_str) - 1

                if len(current_line) == start_index + len(next_num_str) + 1:
                    end_index = len(current_line)
                else:
                    end_index = start_index + len(next_num_str) + 1
                    if start_index != 0 or current_line.find(next_num_str) != 0:
                        end_index += 1


                # print(next_num_str+' -> '+str(start_index)+' '+str(end_index))
                symbol_found_in_vicinity = False
                if i != 0:
                    # find in previous row
                    try:
                        prev_line = lines[i-1][start_index:end_index]
                        # print('prev_line')
                        # print(prev_line)
                        for char in prev_line:
                            if char == '*':
                                gears.append([i-1, start_index+prev_line.find('*'), int(next_num_str)])
                            if not char.isalnum() and char != '.':
                                symbol_found_in_vicinity = True
                    finally:
                        if symbol_found_in_vicinity:
                            print('ADDING: '+next_num_str)
                            total_sum += int(next_num_str)
                if i != (len(lines)-1) and not symbol_found_in_vicinity:
                    # find in next row
                    try:
                        next_line = lines[i+1][start_index:end_index]
                        # print('next_line')
                        # print(next_line)
                        for char in next_line:
                            if char == '*':
                                gears.append([i+1, start_index+next_line.find('*'), int(next_num_str)])
                            if not char.isalnum() and char != '.':
                                symbol_found_in_vicinity = True
                    finally:
                        if symbol_found_in_vicinity:
                            print('ADDING: '+next_num_str)
                            total_sum += int(next_num_str)

                if (not current_line[start_index].isalnum() and not current_line[start_index] == '.' or
                    not current_line[end_index-1].isalnum() and not current_line[end_index-1] == '.'):
                    # find in current row
                    if current_line[start_index] == '*':
                        gears.append([i, start_index, int(next_num_str)])
                    if current_line[end_index - 1] == '*':
                        gears.append([i, end_index - 1, int(next_num_str)])
                    if not symbol_found_in_vicinity:
                        print('ADDING: ' + next_num_str)
                        total_sum += int(next_num_str)

                skip_no = start_index - j + len(next_num_str)
    print(gears)

    multiplicator_dict = {}
    for i in range(len(gears)):

        if not multiplicator_dict.get(gears[i][0]):
            multiplicator_dict[gears[i][0]] = { gears[i][1]: [gears[i][2]] }
        else:
            if not multiplicator_dict[gears[i][0]].get(gears[i][1]):
                multiplicator_dict[gears[i][0]][gears[i][1]] = [ gears[i][2] ]
            else:
                multiplicator_dict[gears[i][0]][gears[i][1]].append(gears[i][2])

    print(multiplicator_dict)

    for row in multiplicator_dict.keys():
        for col in multiplicator_dict[row].keys():
            if len(multiplicator_dict[row][col]) == 2:
                total_gear_sum += multiplicator_dict[row][col][0] * multiplicator_dict[row][col][1]

    print('Total gear sum: '+str(total_gear_sum))
    return total_sum


if __name__ == '__main__':
    print(solution())

import helper
def solution():
    with open('data2') as file:
        lines = [line.strip() for line in file]

    total_sum = 0
    starting_seeds = [] # 79 14 55 13

    seed_list_str = lines[0][lines[0].find(':')+2:].strip()
    for number in seed_list_str.split(' '):
        starting_seeds.append(int(number))
    # print(starting_seeds)

    result_array = helper.parse_input(lines[2:])

    fixed_map = helper.solve_overlaps(result_array)

    # print(fixed_map)

    location_list = []

    for seed in starting_seeds:
        location_list.append(helper.get_location_from_seed(fixed_map, seed))

    print(location_list)

    # location_list = []

    # for seed in starting_seeds:
    #     location_list.append(helper.get_location_from_seed(result_map, seed))
    # print(location_list)

    # return min(location_list)
    return min(location_list)

if __name__ == '__main__':
    print(solution())

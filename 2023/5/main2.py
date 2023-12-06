import helper


def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    total_sum = 0
    starting_seeds = []  # 79 14 55 13

    seed_list_str = lines[0][lines[0].find(':') + 2:].strip()
    for number in seed_list_str.split(' '):
        starting_seeds.append(int(number))

    ######################################################################
    ################ WE ARE TALKING ABOUT SEEDS!!!!!!!$$$$$$$$$$$$$$$$$$$$
    ######################################################################

    starting_seeds_second_part = []  # 79(and 14 number onwards) 55(13 numbers onwards)

    seed_list_second_part_str = lines[0][lines[0].find(':') + 2:].strip()
    for i in range(len(seed_list_second_part_str.split(' '))):
        if i % 2 == 0:
            continue
        first_in_line = int(seed_list_second_part_str.split(' ')[i - 1].strip())
        repetitions = int(seed_list_second_part_str.split(' ')[i].strip())
        x = helper.SeedObject(first_in_line, repetitions)
        # last, first, 0(because the value is the number itself - HERE W
        starting_seeds_second_part.append(x)
    # print(starting_seeds_second_part)
    # print(f'New starting seeds: {starting_seeds_second_part}')
    # will be split into groups, will create map for each name
    # then take the lowest possible
    ######################################################################

    result_array = helper.parse_input(lines[2:])

    fixed_map = helper.solve_overlaps(result_array)

    fixed_starting_seeds_second_part = helper.seeds_split_into_groups(fixed_map, starting_seeds_second_part)

    # for group in fixed_starting_seeds_second_part:
    #     print(f'Starts of each group: {group.start})')
    #     print(f'This seed is in the end: {helper.get_location_from_seed(fixed_map, group.start)}')
    # print(fixed_starting_seeds_second_part)

    # print(fixed_starting_seeds_second_part)



    final_minimized_seeds = []
    final_locations = []
    for group in fixed_starting_seeds_second_part:
        final_minimized_seeds.append(group['start'].start)
        final_locations.append(group['current'].start)

    print(final_minimized_seeds)
    print(final_locations)

    combined_arrays = list(zip(final_minimized_seeds, final_locations))

    # Sort based on the values of the first array
    sorted_combined_arrays = sorted(combined_arrays, key=lambda x: x[0])

    # Extract the second array in the order of the sorted indices
    sorted_array2 = [element[1] for element in sorted_combined_arrays]

    # Print the result
    print("Sorted array1:", [element[0] for element in sorted_combined_arrays])
    print("Corresponding sorted array2:", sorted_array2)

    # new_final_locations = []
    #
    # for seed in new_final_seeds:
    #     new_final_locations.append(helper.get_location_from_seed(fixed_map, seed))

    return min(final_locations)


if __name__ == '__main__':
    print(solution())
[114264781, 986162929, 1079360498, 549819300, 3183462181, 1943688394, 1132285750, 1177713804, 843633210, 2821086308, 502075018, 2836885312, 2880041567, 1668703728, 1717341073, 61038833, 1921754120, 1931878947, 1540050181, 1584154696, 1792937741, 1808916293, 2693179996, 2728251289, 2728884755, 2807427903, 2090752257, 2129639138, 2183555927, 5844012, 60306021, 578962451, 579602486, 602136728, 1727059750, 1752227742, 758183681, 828874610, 516841575, 547630070, 2742958121, 2773388954, 3836386950, 3897837549, 1636521741, 1652173887, 3089574276, 3106586753, 1588972208, 1601241398, 1609022365, 76375284, 79863829, 2250347228, 2272547103, 25043344, 56197024]
[3853741770, 4104994517, 558196027, 1623045508, 3833664421, 887862361, 1230040740, 1724616659, 946120886, 3384156939, 3976602196, 1460360716, 2534128701, 664041710, 3356068546, 861012996, 825516882, 3266889914, 2675077212, 3991368753, 3328175122, 712679055, 2840087745, 1739593580, 226439822, 2719181727, 1916994259, 3183376440, 3116585139, 4217167942, 1659737779, 521152811, 3010934736, 3420588827, 3761811960, 2731120471, 3576635780, 2431553842, 1489132624, 1955881140, 1163080465, 4236367274, 1527193957, 1856022817, 206777808, 222429954, 1839010340, 1232230400, 1096887697, 1694669826, 1193511298, 4270406223, 1588644556, 1833822942, 1232230400, 1663516146, 1109156887]
206777808
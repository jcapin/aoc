import copy

class IndexPair:
    def __init__(self, first):
        self.start = first
        self.finish = -1

    def set_second(self, second):
        self.finish = second

    def print(self):
        print(f"Pair -> {self.start},{self.finish}")


class VIPObject:
    def __init__(self, destination, source, length):
        self.start = source
        self.finish = source + length
        self.value = destination - source

    def overlap(self, before, after):
        #     4 5 6 7 8 9     |      2 3 4 5    (before : 2)
        #     4 5 6 7 8 9     |      7 8 9 10    (after : 3)

        # before means that another number will cover "first" part of the area
        # after means that another number will cover "second" part of the area
        if before > 0:
            self.start += before
        if after > 0:
            self.finish -= after

    def is_same(self, x):
        if self.start == x.start and self.finish == x.finish and self.value == x.value:
            return True
        return False

    def print(self):
        print(f"Pair -> {self.start},{self.finish}")


class SeedObject:
    def __init__(self, start, followers):
        self.start = start
        self.followers = followers

    def split(self, new_groups_indexes):
        # split_indexes are indexes from which it will split:

        # will just send all start/finishes that are in range of (start,start+followers), and then you split by that
        #     start=4, followers=8
        #     4 5 6 7 8 9 10 11
        # split([5,8]) ===>  4 | 5 6 7 | 8 9 10 11

        return_array = []
        if len(new_groups_indexes) == 0:
            return [self]

        for i in range(len(new_groups_indexes)):
            if i == 0:
                # put first inside
                new_group = SeedObject(self.start, new_groups_indexes[i])
                return_array.append(new_group)
            else:
                new_group = SeedObject(self.start+new_groups_indexes[i-1], new_groups_indexes[i]-new_groups_indexes[i-1])
                return_array.append(new_group)
        # put last
        new_group = SeedObject(self.start+new_groups_indexes[-1], self.followers-new_groups_indexes[-1])
        return_array.append(new_group)


        return return_array

    def put_through_one_map(self, map, name_level):
        # ovo se mijenja
        calculated = copy.deepcopy(self)
        x = self.start
        for vip in map[name_level]:
            if vip.start <= x < vip.finish:
                x += vip.value
                break
        calculated.start = x
        return calculated

def parse_input(lines):
    names = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
             'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

    total_map = {}
    index_pairs = []

    for i in range(len(lines)):
        x = lines[i].split(' ')[0]
        if lines[i].split(' ')[0] in names:
            new_pair = IndexPair(i + 1)
            index_pairs.append(new_pair)
            if len(index_pairs) > 1:
                index_pairs[-2].set_second(i - 1)
        index_pairs[-1].set_second(i+1)
    for i in range(len(names)):
        total_map[names[i]] = parse_numbers_to_map(lines[index_pairs[i].start:index_pairs[i].finish])

    return total_map

    # data is all lines below starting seeds


def parse_numbers_to_map(data):
    return_array = []
    for line in data:
        # for each line of numbers
        numbers = line.split(' ')
        for x in numbers:
            if x.strip() == '':
                numbers.remove(x)
        destination_start = int(numbers[0])
        source_start = int(numbers[1])
        range_num = int(numbers[2])

        x = VIPObject(destination_start, source_start, range_num)

        return_array.append(x)

    return return_array


def solve_overlaps(map):
    new_map = {}
    flag_changed = False
    for name in map.keys():
        fixed_overlaps = []
        for vip in map[name]:
            if len(fixed_overlaps) == 0:
                fixed_overlaps.append(vip)
                continue
            for added in fixed_overlaps:
                if vip.is_same(added):
                    break
                # if vip.start <= added.start and vip.finish >= added.finish:
                #     # already added     |----------|
                #     # vip             |--------------|
                #     # RESULT          |--------------| (new)
                #     print(f'VIP REPLACING: ({vip.start}-{vip.finish}) ALREADY INSIDE: ({added.start}-{added.finish}')
                #     fixed_overlaps.remove(added)
                #     continue
                if vip.start <= added.start and vip.finish <= added.finish:
                    # already added     |-----------|
                    # vip             |-----------|
                    # RESULT          |-----------| (new)
                    #                             |-|(old)
                    added.overlap(vip.finish - added.start, 0)
                    continue
                if vip.start >= added.start and vip.finish >= added.finish:
                    # already added   |-----------|
                    # vip               |-----------|
                    # RESULT            |-----------| (new)
                    #                 |-|(old)
                    added.overlap(0, added.finish - vip.start)
                    continue
                # if vip.start >= added.start and vip.finish < added.finish:
                #     # already added   |-----------|
                #     # new               |-------|
                #     # RESULT            |-------| (new)
                #     #                 |-|(old)  |-|(old2)
                #     print(f'VIP REPLACING: ({vip.start}-{vip.finish}) ALREADY INSIDE: ({added.start}-{added.finish}')
                #     second_part_of_area = copy.deepcopy(added)
                #     added.overlap(0, added.finish - vip.start)
                #     second_part_of_area.overlap(vip.finish - added.start, 0)
                #     fixed_overlaps.append(second_part_of_area)
                #     continue
            fixed_overlaps.append(vip)
        new_map[name] = fixed_overlaps
    return new_map


def seeds_split_into_groups(fixed_map, list_seeds):
    biggest_mf_array_of_groups = []  # this will be actually [ {'start': seedGrp, 'current': seedGrp}, {'start': seedGrp, 'current': seedGrp}]
    for seed_group in list_seeds:
        group = {'start': seed_group, 'current': seed_group}
        biggest_mf_array_of_groups.append(group)

    for name in fixed_map.keys():
        for group in biggest_mf_array_of_groups:
            if group['current'].followers == 1:
                continue
            indexes_which_will_split_group = []

            for vip in fixed_map[name]:
                if group['current'].start < vip.start < (group['current'].start + group['current'].followers):
                    # for each transverzation, see if any of seed groups split into more groups
                    # print(f'Vip-start {vip.start} FOUND in: group('+str(group['current'].start)+','+str(group['current'].followers)+')')
                    indexes_which_will_split_group.append(vip.start - group['current'].start)

                if group['current'].start < vip.finish < (group['current'].start + group['current'].followers):
                    # print(f'Vipfinish {vip.finish-1} FOUND in: group('+str(group['current'].start)+','+str(group['current'].followers)+')')
                    indexes_which_will_split_group.append(vip.finish - group['current'].start)
            # print(f'At level {name} and for group there are {indexes_which_will_split_group}')
            indexes_which_will_split_group = list(dict.fromkeys(indexes_which_will_split_group))
            if len(indexes_which_will_split_group) == 0:
                continue
            indexes_which_will_split_group.sort()
            new_groups_instead_of_current_group = group['current'].split(indexes_which_will_split_group)
            new_groups_instead_of_starting_group = group['start'].split(indexes_which_will_split_group)

            if len(new_groups_instead_of_current_group) == 1:
                continue

            biggest_mf_array_of_groups.remove(group)

            for i in range(len(new_groups_instead_of_starting_group)):
                new_group = {'start': copy.deepcopy(new_groups_instead_of_starting_group[i]),
                             'current': copy.deepcopy(new_groups_instead_of_current_group[i])}
                biggest_mf_array_of_groups.append(new_group)

        for seed_group in biggest_mf_array_of_groups:
            seed_group['current'] = seed_group['current'].put_through_one_map(fixed_map, name)

    return biggest_mf_array_of_groups


def get_location_from_seed(map, seed):
    # ovo se mijenja
    x = seed
    for name in map.keys():
        for vip in map[name]:
            if vip.start <= x < vip.finish:
                x += vip.value
                break
        # print(f'{name} to {x}')
    return x

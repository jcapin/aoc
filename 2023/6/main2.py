import re
def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    map_race_len_to_record_distance = {}
    temp_array = lines[0][lines[0].find(':')+1:].strip().split('  ')
    temp_array_2 = lines[1][lines[1].find(':')+1:].strip().split('  ')

    for nr in temp_array:
        if nr.strip() == '':
            temp_array.remove(nr)

    for nr in temp_array_2:
        if nr.strip() == '':
            temp_array_2.remove(nr)

    time_connected = ''
    for nr in temp_array:
        time_connected += nr.strip()
    record_connected = ''
    for nr in temp_array_2:
        record_connected += nr.strip()

    map_race_len_to_record_distance[int(time_connected)] = int(record_connected)

    total_multi = 1

    for race in map_race_len_to_record_distance:
        win_options = []
        for i in range(race+1):
            # print(f'I boost untill min {i}')
            # print(f'I got up to speed {i} and I will travel for {race-i} seconds like that == {abs(i) * abs(race-i)}mm')
            if abs(i) * abs(race-i) > map_race_len_to_record_distance[race]:
                win_options.append(abs(i) * abs(race-i))
        total_multi *= len(win_options)
        # print(win_options)

    print(total_multi)

    # print(map_race_len_to_record_distance)

if __name__ == '__main__':
    print(solution())

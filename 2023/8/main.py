def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    sequence = lines[0]

    tree = {}

    for line in lines[2:]:
        key, value = line.split('=')

        key = key.strip()
        value = tuple(val.strip() for val in value[2:-1].split(','))

        tree[key] = value

    iterator = 0
    current = 'AAA'
    counter = 0
    while True:
        if current == 'ZZZ':
            break
        if iterator == len(sequence):
            iterator = 0
            continue
        if sequence[iterator] == 'L':
            current = tree[current][0]
        else:
            current = tree[current][1]
        counter += 1
        iterator += 1

    print('Counter: '+str(counter))

    # print(tree)
    return 0


if __name__ == '__main__':
    print(solution())

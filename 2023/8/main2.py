import math

def do_all_end_on_z(list):
    for node in list:
        if not node.endswith('Z'):
            return False
    return True
def find_lowest_multiple(numbers):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    result = numbers[0]

    for num in numbers[1:]:
        result = lcm(result, num)

    return result

def solution():
    with open('data') as file:
        lines = [line.strip() for line in file]

    sequence = lines[0]

    tree = {}

    current_nodes = []

    for line in lines[2:]:
        key, value = line.split('=')

        key = key.strip()

        if key.endswith('A'):
            current_nodes.append(key)

        value = tuple(val.strip() for val in value[2:-1].split(','))

        tree[key] = value


    counters = []
    for i in range(len(current_nodes)):
        counters.append(0)

    for i in range(len(current_nodes)):
        iterator = 0
        while True:
            if current_nodes[i].endswith('Z'):
                break
            if iterator == len(sequence):
                iterator = 0
                continue
            if sequence[iterator] == 'L':
                current_nodes[i] = tree[current_nodes[i]][0]
            else:
                current_nodes[i] = tree[current_nodes[i]][1]
            counters[i] += 1
            iterator += 1

    print('Counter: '+str(find_lowest_multiple(counters)))

    # print(tree)
    return 0


if __name__ == '__main__':
    print(solution())

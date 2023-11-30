def solution():
    # length l
    # width w
    # height h
    # l x w x h
    file = open('data', 'r')
    input = file.readlines()
    totalArea = 0

    for i in range(len(input)):
        dimensions = input[i].split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        first = l * w
        second = w * h
        third = l * h
        min = first if (first < second and first < third) else second if (second < first and second < third) else third
        totalArea += 2*first + 2*second + 2*third + min
        # print('first:'+str(first)+' second:'+str(second)+' third:'+str(third)+' min:'+str(min))
        # print(totalArea)

    return totalArea

    return totalArea;
if __name__ == '__main__':
    print(solution())
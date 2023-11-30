def solution():
    file = open('data', 'r')
    input = file.readline().lower()
    counter = 0
    for i in range(len(input)):
        if (input[i] == '('):
            counter+=1
        elif (input[i] == ')'):
            if(counter == 0):
                # entering basement!
                print(i+1) #index of first step that goes into basement
            counter-=1
    return counter

if __name__ == '__main__':
    print(solution())
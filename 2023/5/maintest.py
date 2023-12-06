# will just send all start/finishes that are in range of (start,start+followers), and then you split by that
        #     start=4, followers=8
        #     4 5 6 7 8 9 10 11
        # split([5,8]) ===>  4 | 5 6 7 | 8 9 10 11
import helper

def solution():
    x = helper.SeedObject(4, 8)
    y = x.split([1, 4])
    print(y)


if __name__ == '__main__':
    print(solution())

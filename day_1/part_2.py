from collections import Counter

from part_1 import read_input

def solution(list_1, list_2):
    count = Counter(list_2)
    return sum([count[one]*one for one in list_1])

if __name__ == '__main__':
    print(solution(*read_input('inp/day_one.txt')))
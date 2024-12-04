def read_input(filename):
    list_1 = []
    list_2 = []
    with open(filename) as f:
        for line in f.readlines():
            split = line.split()
            list_1.append(int(split[0]))
            list_2.append(int(split[1]))
    return list_1, list_2

def solution(list_1, list_2):
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    return sum([abs(one - two) for one, two in zip(list_1, list_2)])

print(solution(*read_input('inp/day_one.txt')))
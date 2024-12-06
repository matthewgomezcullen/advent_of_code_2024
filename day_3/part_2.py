import re

from part_1 import read_input, solution as part_1_solution


ENABLERS = r"do\(\)|don't\(\)"


def solution(s: str):
    total = 0
    matches = re.finditer(ENABLERS, s)
    i = 0
    j = 0
    do = True
    for match in matches:
        if match.group() == "do()" and not do:
            do = True
            i = match.start()
        if match.group() == "don't()" and do:
            do = False
            j = match.start()
            total += part_1_solution(s[i:j])
    if do:
        j = len(s)
        total += part_1_solution(s[i:j])
    return total


if __name__ == "__main__":
    print(solution(read_input("inp/day_3.txt")))
    # print(solution("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))

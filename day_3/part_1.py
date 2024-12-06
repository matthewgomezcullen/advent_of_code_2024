import re


MULTIPLIERS = r"mul\(\d{1,3},\d{1,3}\)"


def read_input(file_path):
    with open(file_path, "r") as f:
        return "".join(f.readlines())


def solution(s: str):
    matches = re.findall(MULTIPLIERS, s)
    return sum(
        [a * b for a, b in [map(int, match[4:-1].split(",")) for match in matches]]
    )


if __name__ == "__main__":
    print(solution(read_input("inp/day_3.txt")))
    # print(solution("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))

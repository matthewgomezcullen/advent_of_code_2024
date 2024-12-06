from typing import Literal


def read_input(filename):
    with open(filename) as f:
        return [list(map(int, line.split(" "))) for line in f.readlines()]


def is_valid(report: list[int]):
    direction: Literal["increasing"] | Literal["decreasing"] = (
        "increasing" if report[1] > report[0] else "decreasing"
    )
    if not (1 <= abs(report[1] - report[0]) <= 3):
        return False
    for i in range(1, len(report) - 1):
        if direction == "increasing" and (
            report[i] > report[i + 1] or not (1 <= report[i + 1] - report[i] <= 3)
        ):
            return False
        if direction == "decreasing" and (
            report[i] < report[i + 1] or not (1 <= report[i] - report[i + 1] <= 3)
        ):
            return False
    else:
        return True


def solution(reports: list[list[int]]):
    return sum(map(is_valid, reports))


if __name__ == "__main__":
    print(solution(read_input("inp/day_2.txt")))
    # print(solution([
    #     [7, 6, 4, 2, 1],
    #     [1, 2, 7, 8, 9],
    #     [9, 7, 6, 2, 1],
    #     [1, 3, 2, 4, 5],
    #     [8, 6, 4, 4, 1],
    #     [1, 3, 6, 7, 9]
    # ]))

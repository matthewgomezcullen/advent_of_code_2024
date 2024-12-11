from part_1 import read_input, is_valid


def _is_valid(report: list[int]):
    if is_valid(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_valid(modified_report):
            return True
    return False


def solution(reports: list[list[int]]):
    return sum(map(_is_valid, reports))


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
    # answer: 4
import re


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def solution(lines: list[str]) -> int:
    line_length = len(lines[0])

    def matches(row: int, col) -> int:
        count = 0
        if col + 3 < line_length and lines[row][col : col + 4] in ["XMAS", "SAMX"]:
            count += 1
        if row + 3 < len(lines) and "".join(
            [lines[row + i][col] for i in range(4)]
        ) in ["XMAS", "SAMX"]:
            count += 1
        if (
            row + 3 < len(lines)
            and col + 3 < line_length
            and "".join([lines[row + i][col + i] for i in range(4)]) in ["XMAS", "SAMX"]
        ):
            count += 1
        if (
            row + 3 < len(lines)
            and col - 3 >= 0
            and "".join([lines[row + i][col - i] for i in range(4)]) in ["XMAS", "SAMX"]
        ):
            count += 1
        return count

    # xmas_regex = (
    #     r"XMAS|SAMX|"
    #     r"X" + "." * (line_length) + "M" + "." * (line_length) + "A" + "." * (line_length) + "S|"
    #     r"S" + "." * (line_length) + "A" + "." * (line_length) + "M" + "." * (line_length) + "X|"
    #     r"X" + "." * (line_length + 1) + "M" + "." * (line_length + 1) + "A" + "." * (line_length + 1) + "S|"
    #     r"S" + "." * (line_length + 1) + "A" + "." * (line_length + 1) + "M" + "." * (line_length + 1) + "X|"
    #     r"X" + "." * (line_length - 1) + "M" + "." * (line_length - 1) + "A" + "." * (line_length - 1) + "S|"
    #     r"S" + "." * (line_length - 1) + "A" + "." * (line_length - 1) + "M" + "." * (line_length - 1) + "X"
    # )
    count = 0
    for row in range(len(lines)):
        for col in range(line_length):
            count += matches(row, col)
    return count


if __name__ == "__main__":
    print(solution(read_input("inp/day_4.txt")))
    # print(
    #     solution(
    #         [
    #             "MMMSXXMASM",
    #             "MSAMXMSMSA",
    #             "AMXSXMAAMM",
    #             "MSAMASMSMX",
    #             "XMASAMXAMM",
    #             "XXAMMXXAMA",
    #             "SMSMSASXSS",
    #             "SAXAMASAAA",
    #             "MAMMMXMMMM",
    #             "MXMXAXMASX",
    #         ]
    #     )
    # )
    # answer: 18

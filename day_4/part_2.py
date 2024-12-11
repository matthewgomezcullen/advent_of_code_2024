from part_1 import read_input


def solution(lines: list[str]) -> int:
    count = 0

    for row, line in enumerate(lines[1:-1], 1):
        for col, char in enumerate(line[1:-1], 1):
            if char != "A":
                continue
            if (
                (lines[row - 1][col - 1] == "S" and lines[row + 1][col + 1] == "M")
                or (lines[row - 1][col - 1] == "M" and lines[row + 1][col + 1] == "S")
            ) and (
                (lines[row - 1][col + 1] == "S" and lines[row + 1][col - 1] == "M")
                or (lines[row - 1][col + 1] == "M" and lines[row + 1][col - 1] == "S")
            ):
                count += 1

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
    # answer: 9

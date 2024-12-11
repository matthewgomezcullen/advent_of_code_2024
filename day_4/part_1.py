import re


def read_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def solution(s: str) -> int:
    line_length = s.index("\n")
    s = s.replace("\n", "")
    print(line_length, s)
    xmas_regex = (
        r"XMAS|SAMX|"
        r"X" + "." * (line_length) + "M" + "." * (line_length) + "A" + "." * (line_length) + "S|"
        r"S" + "." * (line_length) + "A" + "." * (line_length) + "M" + "." * (line_length) + "X|"
        r"X" + "." * (line_length + 1) + "M" + "." * (line_length + 1) + "A" + "." * (line_length + 1) + "S|"
        r"S" + "." * (line_length + 1) + "A" + "." * (line_length + 1) + "M" + "." * (line_length + 1) + "X|"
        r"X" + "." * (line_length - 1) + "M" + "." * (line_length - 1) + "A" + "." * (line_length - 1) + "S|"
        r"S" + "." * (line_length - 1) + "A" + "." * (line_length - 1) + "M" + "." * (line_length - 1) + "X"
    )
    print(xmas_regex)
    matches = re.findall(xmas_regex, s)
    print(matches)
    return len(matches)
    


if __name__ == "__main__":
    # print(solution(read_input("inp/day_4.txt")))
    print(
        solution(
"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        )
    )

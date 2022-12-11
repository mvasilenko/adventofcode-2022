from collections import defaultdict


def part1(data, part=1):
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    rows = len(data)
    cols = len(data[0])
    res = 0
    for row in range(rows):
        for col in range(cols):
            for (delta_c, delta_r) in directions:
                col_check = col+delta_c
                row_check = row+delta_r
                max_height = -1
                while 0 <= col_check < cols and 0 <= row_check < rows:
                    max_height = max(max_height, data[row_check][col_check])
                    col_check += delta_c
                    row_check += delta_r
                if part == 1:
                    if max_height < data[row][col]:
                        res += 1
                        break
    print(res)


def part2(data):
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    rows = len(data)
    cols = len(data[0])
    max_score = 0
    for row in range(rows):
        for col in range(cols):
            cur_score = 1
            for (delta_c, delta_r) in directions:
                dir_score = 0
                col_check = col+delta_c
                row_check = row+delta_r
                while 0 <= col_check < cols and 0 <= row_check < rows:
                    if data[row_check][col_check] >= data[row][col]:
                        dir_score += 1
                        break
                    else:
                        dir_score += 1
                    col_check += delta_c
                    row_check += delta_r
                cur_score *= dir_score
            max_score = max(max_score, cur_score)
    print(max_score)


if __name__ == "__main__":
    with open("input-day-08.txt", "r") as f:
        data = f.read().splitlines()
        data = [[int(x) for x in row]
                for row in data]  # split to 99 x 99 2d-array
        part1(data)
        part2(data)

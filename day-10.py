part2_answer = """
####.#..#...##.####.###....##.####.####.
...#.#.#.....#.#....#..#....#.#.......#.
..#..##......#.###..###.....#.###....#..
.#...#.#.....#.#....#..#....#.#.....#...
#....#.#..#..#.#....#..#.#..#.#....#....
####.#..#..##..#....###...##..#....####.
"""


def parse(line):
    if line == "noop":
        return ("noop", 0)
    array = line.split(' ')
    return (array[0], int(array[1]))


def draw(value):
    var = int('111', 2)
    print(bin(var << value))


def part1(data):
    x = 1
    result = 0
    cycle = 0

    def add_cycle():
        nonlocal cycle, result
        cycle += 1
        if (cycle-20) % 40 == 0:
            result += cycle * x

    for line in data:
        instr, arg = parse(line)
        if instr == "addx":
            add_cycle()
            add_cycle()
            x += arg
        elif instr == "noop":
            add_cycle()
        else:
            raise Exception("Wrong instuction, addx/noop expected")
    print(result)


def part2(data):  # ZKJFBJFZ
    x = 1
    result = 0
    cycle = 0
    crt = [['.']*40 for _ in range(6)]

    def draw():
        row = crt[cycle//40]
        col = cycle % 40
        if x-1 <= col <= x+1:
            row[col] = "#"

    for line in data:
        instr, arg = parse(line)
        if instr == "addx":
            draw()
            cycle += 1
            draw()
            cycle += 1
            x += arg
        elif instr == "noop":
            draw()
            cycle += 1
        else:
            raise Exception("Wrong instuction, addx/noop expected")

    result = "\n" + "\n".join("".join(line) for line in crt) + "\n"
    return result


if __name__ == "__main__":
    with open("input-day-10.txt", "r") as f:
        data = f.read().splitlines()
        print(part2_answer)
        print(part2(data))
        # part1(data)
        assert part2_answer == part2(data)

def head_move(head_pos, direction):
    head_x, head_y = head_pos
    if direction == "L":
        pos = (head_x - 1, head_y)
    elif direction == "R":
        pos = (head_x + 1, head_y)
    elif direction == "U":
        pos = (head_x, head_y + 1)
    elif direction == "D":
        pos = (head_x, head_y - 1)
    else:
        raise Exception("Wrong direction move, U/D/L/R expected")
    return pos


def tail_move(head_pos, tail_pos):
    dx = head_pos[0] - tail_pos[0]
    dy = head_pos[1] - tail_pos[1]
    if abs(dx) <=1 and abs(dy) <= 1:
        dx=0
        dy=0
    else:
        if abs(dx)>=2:
            if dx>0:
                dx = 1
            else:
                dx = -1
        if abs(dy)>=2:
            if dy>0:
                dy = 1
            else:
                dy = -1

    tail_new_x = tail_pos[0]+dx
    tail_new_y = tail_pos[1]+dy
    return (tail_new_x, tail_new_y)


def part1(movements):
    visited = set()
    head_pos = (0,0)
    tail_pos = (0,0)
    for direction, steps in movements:
        for _ in range(steps):
            head_pos = head_move(head_pos, direction)
            tail_pos = tail_move(head_pos, tail_pos)
            visited.add(tail_pos)
    print(visited)
    print(len(visited))

def part2(movements):
    rope = [(0,0)]* 10
    visited = set()
    head_pos = (0,0)
    tail_pos = (0,0)
    for direction, steps in movements:
        for _ in range(steps):
            rope2 = [head_move(rope[0], direction)]
            for r in rope[1:]:
                rope2.append(tail_move(rope2[-1], r))
            rope = rope2
            visited.add(rope[-1])
    print(visited)
    print(len(visited))


def parse(line):
    array = line.split(' ')
    return (array[0], int(array[1]))

if __name__ == "__main__":
    with open("input-day-09.txt", "r") as f:
        data = f.read().splitlines()
        movements = [parse(line) for line in data]
        part1(movements)
        part2(movements)

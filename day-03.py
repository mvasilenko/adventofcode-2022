from collections import defaultdict

prio_map = dict()


def var_init():
    for c in range(ord('a'), ord('z')+1):
        prio_map[chr(c)] = c - ord('a') + 1  # a:1..z:26
    for c in range(ord('A'), ord('Z')+1):
        prio_map[chr(c)] = c - ord('A') + 27  # A:27..Z:52


def main():
    with open("input-day-03.txt", 'r') as f:
        data = f.read().splitlines()

    var_init()
    result = 0
    for line in data:
        pivot = len(line) // 2
        s1 = set(line[:pivot])
        s2 = set(line[pivot:])
        common = ''.join(s1 & s2)
        result += prio_map[common]
    print(result)

    i, result = 0, 0
    while i < len(data):
        s1 = set(data[i])
        s2 = set(data[i+1])
        s3 = set(data[i+2])
        common = s1 & s2 & s3
        result += prio_map[next(iter(common))]
        i += 3
    print(result)


if __name__ == "__main__":
    main()

from collections import defaultdict


def main(n):

    with open("input-day-06.txt", "r") as f:
        data = f.read()

    map = defaultdict(int)
    for c, v in enumerate(data):
        if c >= n:
            tmp = data[c-n:c]
            tmp_set = set(tmp)
            if len(tmp_set) == n:
                return c


if __name__ == "__main__":
    print(main(4))
    print(main(14))

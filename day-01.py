
def main():
    with open("input-day-01.txt", 'r') as f:
        data = f.read().splitlines()

    callories = 0
    elfs = []
    for c in data:
        if c != '':
            callories += int(c)
        else:
            elfs.append(callories)
            callories = 0
    elfs_sorted = sorted(elfs, reverse=True)
    # elf carrying biggest calories amount
    print(elfs_sorted[0])
    # top 3 elves callories sum
    print(sum(elfs_sorted[:3]))


if __name__ == "__main__":
    main()

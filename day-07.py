from collections import defaultdict


def calculate_folder_sizes(data):
    folders = []
    size = defaultdict(int)
    path = []

    for line in data:
        line_spl = line.split()
        if line_spl[1] == "cd":
            cddir = line_spl[2]
            if cddir == "..":
                path.pop()
            else:
                if path:
                    if path[-1] == '/':
                        sep = ''
                    else:
                        sep = '/'
                    path.append(path[-1] + sep + cddir)
                else:
                    path.append('/')
        elif line_spl[1] == 'ls':
            pass
        else:
            if line_spl[0].isnumeric():
                for i in path:
                    # increase all parent directory sizes
                    size[i] += int(line_spl[0])
    res1 = 0
    for f in size:
        if size[f] < 100000:
            res1 += size[f]
    print(res1)

    total_space = 70000000
    free_space = total_space - max(size.values())
    needed_space = 30000000
    delete_folders = []
    for f in size:
        if free_space + size[f] >= needed_space:
            delete_folders.append(size[f])
    print(min(delete_folders))


if __name__ == "__main__":
    with open("input-day-07.txt", "r") as f:
        data = f.read().splitlines()
        calculate_folder_sizes(data)

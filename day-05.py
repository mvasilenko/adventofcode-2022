num_stacks = 9


def main(day2=False):

    with open("input-day-05.txt", "r") as f:
        data = f.read().splitlines()

    ini = [[] for x in range(num_stacks+1)]
    # print(ini)
    pos = [x*4+1 for x in range(num_stacks)]
    # print(pos)
    for line in data:
        if "[" in line:
            # print(line)
            for i, v in enumerate(pos):
                if line[v].isalpha():
                    ini[i+1] = list(line[v]) + ini[i+1]  # +ini[i+1]
        elif line.startswith("move"):
            _, amount, _, src, _, dst = line.split(" ")
            amount, src, dst = int(amount), int(src), int(dst)
            #print(f"move {amount} from {src} to {dst}")
            #print("ini[src] before",ini[src])
            #print("ini[dst] before", ini[dst])
            tmp = ini[src][len(ini[src])-amount:len(ini[src])]
            # day 2
            if day2:
                tmp = tmp[::-1]
            ini[dst] += tmp
            ini[src] = ini[src][:len(ini[src])-amount]

    ini = ini[1:]
    result = "".join(map(lambda x: x[-1], ini))
    return result


if __name__ == "__main__":
    print(main(day2=False) == 'JNRSCDWPP')
    print(main(day2=True) == 'TWSGQHNHL')

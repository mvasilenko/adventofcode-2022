

def main():

    with open("input-day-04.txt", "r") as f:
        data = f.read().splitlines()

    result1, result2 = 0, 0
    for line in data:
        i = [[int(x) for x in y.split('-')] for y in line.split(',')]

        i1l_in_i2 = i[1][0] <= i[0][0] <= i[1][1]
        i1r_in_i2 = i[1][0] <= i[0][1] <= i[1][1]

        i2l_in_i1 = i[0][0] <= i[1][0] <= i[0][1]
        i2r_in_i1 = i[0][0] <= i[1][1] <= i[0][1]

        if i1l_in_i2 and i1r_in_i2:
            result1 += 1
        elif i2l_in_i1 and i2r_in_i1:
            result1 += 1

        if i1l_in_i2 or i1r_in_i2:
            result2 += 1
        elif i2l_in_i1 or i2r_in_i1:
            result2 += 1

    print(result1)
    print(result2)


if __name__ == "__main__":
    main()

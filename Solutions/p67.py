from p18 import step, main
#depends on p18

data = list()

def solve():
    with open('p067_triangle.txt') as f:
        for line in f.readlines():
            data.append([int(x) for x in line.split()])
    main(data)
    return data[0][0]

print solve()



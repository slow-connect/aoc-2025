import aoc

input = aoc.get_lst(9)[:-1]
input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split("\n")

input = [(int(x), int(y)) for i in input for x, y in [i.split(",")]]


def calculate_surface(x, y):
    return (1 + abs(x[0] - y[0])) * (1 + abs(x[1] - y[1]))


# part 1
n = len(input)
max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        if calculate_surface(input[i], input[j]) > max_area:
            max_area = calculate_surface(input[i], input[j])
print(max_area)

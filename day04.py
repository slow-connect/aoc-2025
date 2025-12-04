import aoc

input = aoc.get_lst(4)[:-1]
# input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.""".split("\n")


def make_map(input):
    top = "#" * (len(input[0]) + 2)
    map = [top]
    for line in input:
        map.append("#" + line + "#")
    map.append(top)
    return map


map = make_map(input)
input = [list(s) for s in input]
accessible = 0


def cnt_free_neibourg(i, j):
    cnt = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == 0 and l == 0:
                continue
            if map[i + k][j + l] != "@":
                cnt += 1
    return cnt


for i in range(1, len(map) - 1):
    for j in range(1, len(map[1]) - 1):
        if map[i][j] != "@":
            continue
        x = cnt_free_neibourg(i, j)
        # input[i - 1][j - 1] = str(x)
        if x >= 5:
            accessible += 1
            # input[i - 1][j - 1] = "X"

# part 1
print(accessible)
# for row in input:
#     print("".join(row))

accessible = 0
while True:
    added = 0
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[1]) - 1):
            if map[i][j] != "@":
                continue
            x = cnt_free_neibourg(i, j)
            if x >= 5:
                added += 1
                input[i - 1][j - 1] = "."
    accessible += added
    map = make_map(["".join(s) for s in input])
    if added == 0:
        break
print(accessible)

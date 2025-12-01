import aoc

input = aoc.get_lst(1)[:-1]
# input = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".split("\n")
dial = 50
module = 100
cnt = 0


# part 1
for i in range(len(input)):
    dir = input[i][0]
    move = int(input[i][1:])
    if dir == "L":
        dial -= move
    elif dir == "R":
        dial += move
    dial = dial % module
    if dial == 0:
        cnt += 1
print("part1: ", cnt)

# part 2
cnt = 0
dial = 50
for i in range(len(input)):
    dir = input[i][0]
    move = int(input[i][1:])
    for _ in range(move):
        if dir == "L":
            dial -= 1
        elif dir == "R":
            dial += 1
        dial = dial % module
        if dial == 0:
            cnt += 1
print("part2: ", cnt)

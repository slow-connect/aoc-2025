from collections import defaultdict

import aoc

input = aoc.get_lst(7)[:-1]
# input = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............""".split("\n")

input = [list(s) for s in input]
input.append(list("." * len(input[0])))

# Part 1
cnt = 0
for i in range(len(input) - 1):
    for j in range(len(input[i])):
        if input[i][j] == "S" or input[i][j] == "|":
            if input[i + 1][j] == "^":
                cnt += 1
                if j == 0:
                    input[i + 1][j + 1] = "|"
                elif j == len(input[i]):
                    input[i + 1][j - 1] = "|"
                else:
                    input[i + 1][j - 1] = "|"
                    input[i + 1][j + 1] = "|"
            else:
                input[i + 1][j] = "|"
print(cnt)

# Part 2
cnt = 1
root = (0, input[0].index("S"))
n = len(input)
dp = defaultdict(int)
dp[root] += 1
for i in range(n - 1):
    ndp = defaultdict(int)
    for (x, y), cur in dp.items():
        if x == n - 1:
            continue
        inc = cur
        if input[x + 1][y] == "^":
            cnt += inc
            ndp[(x + 1, y - 1)] += inc
            ndp[(x + 1, y + 1)] += inc
        else:
            ndp[(x + 1, y)] += inc
    dp = ndp

print(cnt)

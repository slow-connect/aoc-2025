import re
from math import prod

import aoc

input = aoc.get_lst(6)[:-1]
# input = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """.split("\n")


def part1(input):
    input = [re.findall(r"\S+", l) for l in input]
    for j in range(len(input) - 1):
        input[j] = [int(n) for n in input[j]]

    res = 0
    for j in range(len(input[0])):
        opp = input[-1][j]
        if opp == "+":
            res += sum([input[i][j] for i in range(len(input) - 1)])
        else:
            res += prod([input[i][j] for i in range(len(input) - 1)])
    print(res)


n = len(input) - 1
res = 0
opp = "."
lst = []
for j in range(max(len(input[_]) for _ in range(len(input)))):
    if input[-1][j] != " ":
        opp = input[-1][j]
    num = ""
    for i in range(n):
        if len(input[i]) > j:
            num += input[i][j]
    if num == " " * (n):
        if opp == "+":
            res += sum(lst)
        else:
            res += prod(lst)

        lst = []
        continue
    num = int(num.strip())
    lst.append(num)


if opp == "+":
    res += sum(lst)
else:
    res += prod(lst)


print(res)

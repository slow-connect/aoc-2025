import itertools
from itertools import product

import aoc

input = aoc.get_lst(10)[:-1]
# input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split("\n")


cnt = 0
for l in input:
    target, rest = l.split("]")
    target = [1 if t == "#" else 0 for t in target[1:]]
    m = len(target)
    vectors, joltage = rest.split("{")
    vectors = vectors.replace(" ", "")
    vectors = vectors.split(")(")
    vectors = [v.replace("(", "").replace(")", "").split(",") for v in vectors]
    vectors = [[int(a) for a in v] for v in vectors]
    n = len(vectors)
    min = n
    for subset in product([0, 1], repeat=n):
        lst = [0 for _ in range(m)]
        for i in range(n):
            if subset[i] == 1:
                for j in vectors[i]:
                    lst[j] = lst[j] ^ 1

        if lst == target and sum(subset) < min:
            min = sum(subset)
    cnt += min
print(cnt)

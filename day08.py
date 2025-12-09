from collections import Counter

import numpy as np

import aoc

input = aoc.get_lst(8)[:-1]
# input = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689""".split("\n")

input = [(int(x), int(y), int(z)) for i in input for x, y, z in [i.split(",")]]


def euclidian_distance(p, q):
    if len(p) != len(q):
        raise ValueError("same length")
    return sum((i - j) ** 2 for i, j in zip(p, q))


n = len(input)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        distance_matrix[i, j] = euclidian_distance(input[i], input[j])

circuits = {key: None for key in range(n)}


def masked_argmin(m, limit):
    mask = m > limit
    valids = np.min(m[mask])
    return np.argwhere(m == valids)


min_dist = 0
circuits_count = 0

for _ in range(1000):
    shortest = masked_argmin(distance_matrix, min_dist)
    # print(shortest[0], end=" ")
    if len(shortest) != 1:
        print("several with same distance")
    shortest = shortest[0]
    i, j = shortest
    # print(i, j, end=" ")
    min_dist = distance_matrix[i][j]
    # print(circuits)
    if circuits[i] is None and circuits[j] is None:
        circuits[i] = circuits_count
        circuits[j] = circuits_count
        circuits_count += 1
    elif circuits[i] is None:
        circuits[i] = circuits[j]
    elif circuits[j] is None:
        circuits[j] = circuits[i]
    elif circuits[i] == circuits[j]:
        _ - +1
    else:
        change = max(circuits[i], circuits[j])
        keep = min(circuits[i], circuits[j])
        keys = [k for k, v in circuits.items() if v == change]
        for k in keys:
            circuits[k] = keep
counter = Counter(circuits.values())

# part 1
res = 1
cnt = 0
for k, v in sorted(counter.items(), key=lambda i: i[1], reverse=True):
    if cnt == 3:
        break
    if k is None:
        continue
    else:
        cnt += 1
        res *= v
print(res)

# part 2
res = 0
while not all(value == next(iter(circuits.values())) for value in circuits.values()):
    shortest = masked_argmin(distance_matrix, min_dist)
    # print(shortest[0], end=" ")
    if len(shortest) != 1:
        print("several with same distance")
    shortest = shortest[0]
    i, j = shortest
    # print(i, j, end=" ")
    min_dist = distance_matrix[i][j]
    # print(circuits)
    if circuits[i] is None and circuits[j] is None:
        circuits[i] = circuits_count
        circuits[j] = circuits_count
        circuits_count += 1
    elif circuits[i] is None:
        circuits[i] = circuits[j]
    elif circuits[j] is None:
        circuits[j] = circuits[i]
    elif circuits[i] == circuits[j]:
        continue
    else:
        change = max(circuits[i], circuits[j])
        keep = min(circuits[i], circuits[j])
        keys = [k for k, v in circuits.items() if v == change]
        for k in keys:
            circuits[k] = keep
    res = input[i][0] * input[j][0]
print(res)

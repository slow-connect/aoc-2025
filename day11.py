import numpy as np
from tqdm import tqdm

import aoc

input = aoc.get_lst(11)[:-1]
# input = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out""".split("\n")


unique_points = set()
for l in input:
    src, dst = l.split(": ")
    unique_points.add(src)
    dst = dst.split(" ")
    for d in dst:
        unique_points.add(d)
unique_points = list(unique_points)
n = len(unique_points)
you = unique_points.index("you")
out = unique_points.index("out")

graph = np.zeros((n, n), dtype=int)
for l in input:
    src, dst = l.split(": ")
    src = unique_points.index(src)
    dst = dst.split(" ")
    for d in dst:
        graph[src][unique_points.index(d)] = 1

cnt = graph[you][out]
deg = graph
for _ in tqdm(range(n)):
    deg = np.matmul(deg, graph)
    cnt += deg[you][out]

print(cnt)

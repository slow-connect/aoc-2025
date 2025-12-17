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

# input = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out""".split("\n")


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
svr = unique_points.index("svr")
dac = unique_points.index("dac")
fft = unique_points.index("fft")

graph = np.zeros((n, n), dtype=int)
for l in input:
    src, dst = l.split(": ")
    src = unique_points.index(src)
    dst = dst.split(" ")
    for d in dst:
        graph[src][unique_points.index(d)] = 1

# cnt for part 1
cnt = graph[you][out]

# part 1
to_fft = graph[svr][fft]
to_dac = graph[svr][dac]
middle_1 = graph[fft][dac]
middle_2 = graph[dac][fft]
from_dac = graph[dac][out]
from_fft = graph[fft][out]

deg = graph
for _ in tqdm(range(n)):
    deg = np.matmul(deg, graph)
    cnt += deg[you][out]
    to_fft += deg[svr][fft]
    to_dac += deg[svr][dac]
    middle_1 += deg[fft][dac]
    middle_2 += deg[dac][fft]
    from_dac += deg[dac][out]
    from_fft += deg[fft][out]

print(cnt)
# print(to_fft, middle_1, from_dac)
# print(to_dac, middle_2, from_fft)
print(to_fft * middle_1 * from_dac + to_dac * middle_2 * from_fft)

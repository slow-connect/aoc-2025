import portion as P

import aoc

input = aoc.get_lst(5)[:-1]
# input = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32""".split("\n")


## Part 1
fresh_intervals = []
ingredients = False
fresh = 0
for i in range(len(input)):
    if input[i] == "":
        ingredients = True
        continue
    if not ingredients:
        r = input[i].split("-")
        fresh_intervals.append((int(r[0]), int(r[1]) + 1))
    else:
        num = int(input[i])
        for l, r in fresh_intervals:
            if l <= num < r:
                fresh += 1
                break
print(fresh)

## Part 2
fresh_ids = P.empty()
for i in range(len(input)):
    if input[i] == "":
        break
    iv = input[i].split("-")
    l_, r_ = int(iv[0]), int(iv[1])
    fresh_ids = fresh_ids | P.closed(l_, r_)

cnt = 0
for interval in fresh_ids:
    cnt += interval.upper - interval.lower + 1
print(cnt)

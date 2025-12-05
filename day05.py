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
fresh_ids = []
for i in range(len(input)):
    if input[i] == "":
        break
    iv = input[i].split("-")
    l_, r_ = int(iv[0]), int(iv[1])
    fresh_ids.append((l_, r_))

fresh_ids = sorted(fresh_ids, key=lambda x: x[1])

merged_ranges = []
current_range = fresh_ids[-1]
for k in range(len(fresh_ids) - 2, -1, -1):
    if current_range[0] <= fresh_ids[k][1]:
        current_range = (
            min(current_range[0], fresh_ids[k][0]),
            max(current_range[1], fresh_ids[k][1]),
        )
    else:
        merged_ranges.append(current_range)
        current_range = fresh_ids[k]
merged_ranges.append(current_range)
cnt = 0
for interval in merged_ranges:
    cnt += interval[1] - interval[0] + 1
print(cnt)

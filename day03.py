import aoc

input = aoc.get_lst(3)[:-1]
# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".split("\n")

cnt = 0
for l in input:
    cand = 0
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            tmp = l[i] + l[j]
            if int(tmp) > cand:
                cand = int(tmp)
    cnt += cand
print(cnt)


int_list = [[int(n) for n in l] for l in input]
cnt = 0
for l in int_list:
    last = 0
    for i in range(12):
        c = max(l[last : i - 11 if i - 11 < 0 else None])
        last = l.index(c, last) + 1
        cnt += 10 ** (11 - i) * c
print(cnt)

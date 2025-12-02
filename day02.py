import aoc

id_range = aoc.get_str(2)[:-1]
# id_range = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

id_range = id_range.split(",")
id_range = [interval.split("-") for interval in id_range]
id_range = [((int(i), int(j) + 1)) for i, j in id_range]


# part1
cnt = 0
res_list = []
for intervall in id_range:
    for can in range(intervall[0], intervall[1]):
        num = str(can)
        if len(num) % 2 == 0:
            if num[: len(num) // 2] == num[len(num) // 2 :]:
                cnt += can
                res_list.append(can)

# print(res_list)
print(cnt)

cnt = 0
res_list = []
for intervall in id_range:
    for can in range(intervall[0], intervall[1]):
        num = str(can)
        for i in range(1, 13):
            if num == num[:i] * (len(num) // i) and len(num) > i:
                cnt += can
                res_list.append(can)
                break
# print(res_list)
print(cnt)

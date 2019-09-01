n = int(input())
h_list = list(map(int,input().split()))
count = 0
max_count = 0
max_num = 0
for h in h_list[::-1]:
    if max_num <= h:
        count += 1
        max_num = max(max_num, h)
    else:
        max_count = max(max_count, count)
        count = 1
        max_num = 0
max_count = max(max_count, count)
print(max_count-1)
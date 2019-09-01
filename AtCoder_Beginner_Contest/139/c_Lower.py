n = int(input())
h_list = list(map(int,input().split()))
tmp_list = []
count = 0
for i in range(len(h_list)-1):
    if h_list[i] >= h_list[i+1]:
        count += 1
    else:
        tmp_list.append(count)
        count = 0
tmp_list.append(count)
print(max(tmp_list))

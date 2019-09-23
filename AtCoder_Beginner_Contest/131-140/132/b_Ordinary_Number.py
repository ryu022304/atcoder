n = int(input())
p_list = list(map(int,input().split()))
count = 0
for i in range(1,len(p_list)-1):
    tmp_list = [p_list[i-1], p_list[i], p_list[i+1]]
    tmp_list.sort()
    if tmp_list[1] == p_list[i]:
        count += 1
print(count)
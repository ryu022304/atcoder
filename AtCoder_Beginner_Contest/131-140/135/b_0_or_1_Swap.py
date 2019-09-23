n = int(input())
p_list = list(map(int,input().split()))
p_list_s = sorted(p_list)
count = 0
for i in range(len(p_list)):
    if p_list[i] != p_list_s[i]:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')
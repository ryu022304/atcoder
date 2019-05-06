n,m = map(int,input().split())
lrs_list = [list(map(int,input().split())) for _ in range(n)]
res_list = [0]*(m+2)
sum_num = 0
for l,r,s in lrs_list:
    res_list[l] += s
    res_list[r+1] -= s
    sum_num += s

for i in range(1,len(res_list)):
    res_list[i] += res_list[i-1]
res_list.pop(0)
res_list.pop(-1)
print(sum_num-min(res_list))

n,k = map(int,input().split())
res_list = [0]*k
for i in range(n):
    res_list[i%k] += 1
print(max(res_list)-min(res_list))

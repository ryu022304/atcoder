n,k = map(int,input().split())
a_list = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(i,n):
        if a_list[i] > a_list[j]:
            count += 1

tmp_list = [0]*n
for i in range(n):
    cnt = 0
    for a in a_list:
        if a_list[i] > a:
            cnt += 1
    tmp_list[i] = cnt
res = k * (2*count + sum(tmp_list) * (k-1)) // 2 
print(res % (10**9+7))
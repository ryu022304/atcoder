n = int(input())
v_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))
res = []
for i in range(n):
    if v_list[i]-c_list[i] > 0:
        res.append(v_list[i]-c_list[i])
    else:
        continue
print(sum(res))

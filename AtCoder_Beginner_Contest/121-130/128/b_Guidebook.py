n = int(input())
sp_list = [input().split() for _ in range(n)]

tmp = []
for i,sp in enumerate(sp_list,1):
    tmp.append([i,sp[0],int(sp[1])])

sp_list1 = sorted(tmp, key=lambda x: x[2], reverse=True)
sp_list2 = sorted(sp_list1, key=lambda x: x[1], reverse=False)

for i,s,p in sp_list2:
    print(i)
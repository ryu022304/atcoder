n,q = map(int, input().split())
s = list(input())
lr_list = [list(map(int,input().split())) for _ in range(q)]
tmp_list = [0]*(n+1)

for i in range(1,n):
    if s[i-1]=='A' and s[i]=='C':
        tmp_list[i] = tmp_list[i-1]+1
    else:
        tmp_list[i] = tmp_list[i-1]

for l,r in lr_list:
    print(tmp_list[r-1]-tmp_list[l-1])

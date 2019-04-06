n = int(input())
t,a = map(int,input().split())
h_list = list(map(int,input().split()))
tmp = []
for h in h_list:
    tmp.append(t-h*0.006)
res = [abs(a-i) for i in tmp]
print(res.index(min(res))+1)

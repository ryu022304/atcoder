n,a,b = map(int, input().split())
res = []
for i in range(1,n+1):
    num = sum(list(map(int,list(str(i)))))
    if a<= num <= b:
        res.append(i)
print(sum(res))

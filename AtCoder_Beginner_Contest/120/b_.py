a,b,k = map(int,input().split())
count = 0
res = []
for i in range(1,101):
    if a%i == 0 and b%i == 0:
        res.append(i)
print(res[-k])

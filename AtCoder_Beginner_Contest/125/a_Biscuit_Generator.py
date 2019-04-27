a,b,t = map(int,input().split())
res = 0
i = 1
while True:
    if a*i < t+0.5:
        res += b
    else:
        break
    i += 1
print(res)

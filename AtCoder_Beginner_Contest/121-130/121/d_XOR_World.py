a,b = map(int,input().split())
l = list(range(a,b+1))

res = 0
for val in l:
    res = res^val
print(res)

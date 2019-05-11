n = int(input())
#res = [0]*(10**12+1)
res = 0
for i in range(1,n+1):
    q,mod = divmod(n,i)
    if q == mod:
        res += i
print(res)

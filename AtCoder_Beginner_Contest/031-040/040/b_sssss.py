n = int(input())
res = float('inf')
if n == 1:
    print(0)
else:
    for i in range(1,n):
        p,q = divmod(n,i)
        res = min(res, abs(p-i)+q)
    print(res)

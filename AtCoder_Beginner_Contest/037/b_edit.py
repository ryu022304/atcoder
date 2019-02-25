n,q = map(int,input().split())
suuretsu = [map(int,input().split()) for _ in range(q)]
a = [0]*n
for l,r,t in suuretsu:
    a[l-1:r]=[t]*(r-l+1)
for s in a:
    print(s)

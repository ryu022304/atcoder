a,b,c,k = map(int,input().split())
s,t = map(int,input().split())
res = 0
if s+t >= k:
    res = (a-c)*s+(b-c)*t
else:
    res = a*s + b*t
print(res)

w,h,n = map(int,input().split())
pos_list = [map(int,input().split()) for _ in range(n)]
s = [0,0]
f = [w,h]
for x,y,a in pos_list:
    if a == 1:
        s[0] = max(s[0],x)
    elif a == 2:
        f[0] = min(f[0],x)
    elif a == 3:
        s[1] = max(s[1],y)
    elif a == 4:
        f[1] = min(f[1],y)

if f[0]-s[0] <= 0 or f[1] - s[1] <= 0:
    print(0)
else:
    print((f[0]-s[0])*(f[1]-s[1]))

n,t = map(int,input().split())
a = [int(input()) for _ in [0]*n]
total = 0
pre = 0
for i,time in enumerate(a):
    if i == 0:
        pass
    else:
        if t < time-pre:
            total += t
        else:
            total += time-pre
    pre = time
print(total+t)

s = list(input())
t = int(input())
dir = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
now = (0,0)
count = 0
for d in s:
    if d == '?':
        count += 1
        continue
    next = dir[d]
    x,y = now
    now = (x+next[0],y+next[1])
x,y = now
if t == 1:
    print(abs(x)+abs(y)+count)
else:
    print(max(abs(x)+abs(y)-count,(abs(x)+abs(y)-count)%2))

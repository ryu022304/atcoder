txa,tya,txb,tyb,t,v = map(int,input().split())
n = int(input())
xy_list = [list(map(int,input().split())) for _ in range(n)]
f = False
for x,y in xy_list:
    d = ((txa-x)**2+(tya-y)**2)**0.5+((txb-x)**2+(tyb-y)**2)**0.5
    if d <= t*v:
        f = True
        break
print('YES' if f else 'NO')

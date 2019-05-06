import heapq
h,w,t = map(int,input().split())
s_list = [list(input()) for _ in range(h)]
dir = [(0,1),(-1,0),(0,-1),(1,0)]
sx,sy = 0,0
gx,gy = 0,0
for i in range(h):
    for j in range(w):
        if s_list[i][j]=='S':
            sy,sx = i,j
        elif s_list[i][j]=='G':
            gy,gx = i,j

def solve(time):
    heap = [(0,sx,sy)]
    path = [[2*10**10 for _ in range(w)] for _ in range(h)]
    path[sy][sx] = 0
    while len(heap) > 0:
        c,x,y = heapq.heappop(heap)
        for dx,dy in dir:
            nx = dx+x
            ny = dy+y
            if nx >= 0 and nx < w and ny >= 0 and ny < h:
                c_ = c + (time if s_list[ny][nx]=='#' else 1)
                if path[ny][nx] > c_:
                    path[ny][nx] = c_
                    heapq.heappush(heap,(c_,nx,ny))
            else:
                pass
    #import pprint
    #pprint.pprint(path,width=20)
    return path[gy][gx]

lo = 1
hi = t
for _ in range(30):
    mid = (lo+hi)//2
    time = solve(mid)
    if time <= t:
        lo = mid
    else:
        hi = mid
print(lo)

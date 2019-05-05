h,w = map(int,input().split())
a_list = [list(input()) for _ in range(h)]

dis = []
black_list = [(i,j) for i in range(h) for j in range(w) if a_list[i][j]=='#']

for i in range(h):
    for j in range(w):
        if a_list[i][j]=='#':
            dis.append(0)
            continue
        max_dis = 10**6
        for x,y in black_list:
            if max_dis <= 1:
                break
            else:
                max_dis = min(max_dis,abs(x-i)+abs(y-j))
        dis.append(max_dis)
print(max(dis))

'''
import copy
dic = [(0,1),(-1,0),(0,-1),(1,0)]
count = 0
flag = False
res_list = copy.deepcopy(a_list)
while True:
    for i in range(h):
        for j in range(w):
            if a_list[i][j]=='#':
                for x,y in dic:
                    if i+x==-1 or i+x==h or j+y==-1 or j+y==w:
                        continue
                    elif a_list[i+x][j+y]=='.':
                        res_list[i+x][j+y] = '#'
                        flag = True

    if flag:
        count += 1
        flag = False
        a_list = copy.deepcopy(res_list)
    else:
        break
print(count)
'''

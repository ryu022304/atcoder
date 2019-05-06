r,c,k = map(int,input().split())
s_list = [list(input()) for _ in range(r)]
tmp_list = [[0 for _ in range(c+1)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if s_list[i][j]=='x':
            for kk in range(k):
                if i-kk >= 0:
                    tmp_list[i-kk][max(0,j-k+kk+1)] += 1
                    tmp_list[i-kk][min(c,j+k-kk)] -= 1
                if i+kk < r:
                    tmp_list[i+kk][max(0,j-k+kk+1)] += 1
                    tmp_list[i+kk][min(c,j+k-kk)] -= 1

for i in range(r):
    for j in range(1,c+1):
        tmp_list[i][j] += tmp_list[i][j-1]

count = 0
for i in range(k-1,r-k+1):
    for j in range(k-1,c-k+1):
        if tmp_list[i][j]==0:
            count += 1

print(count)

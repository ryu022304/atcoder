r,g,b,n = map(int,input().split())
count = 0
for i in range(n+1):
    for j in range(n+1):
        bk = n-i*r-j*g
        if bk%b == 0 and bk >= 0:
            count += 1
print(count)

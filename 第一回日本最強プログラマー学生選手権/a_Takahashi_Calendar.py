m,d = map(int,input().split())
count = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        if j >= 22:
            d_s = str(j)
            if int(d_s[0])*int(d_s[1])==i and (int(d_s[0])>=2 and int(d_s[1])>=2):
                count += 1
print(count)
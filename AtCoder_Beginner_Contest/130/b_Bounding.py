n,x = map(int,input().split())
l_list = list(map(int,input().split()))

count = 1
res = 0
for l in l_list:
    res += l
    if res <= x:
        count += 1
    else:
        break
print(count)
n = int(input())
a = list(map(int,input().split()))
count = 0
if sum(a)%n != 0:
    print(-1)
else:
    ave = sum(a)//n
    res = 0
    for an in a:
        res += ave - an
        if res != 0:
            count += 1
    print(count)

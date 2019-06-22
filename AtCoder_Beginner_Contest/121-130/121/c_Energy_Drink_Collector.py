n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
sorted_ab = sorted(ab)

now = m
money = 0
for a,b in sorted_ab:
    if b <= now:
        now -= b
        money += a*b
    else:
        money += a*now
        break
print(money)

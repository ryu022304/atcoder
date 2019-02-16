n,s,t = map(int,input().split())
w = int(input())
a = [int(input()) for _ in [0]*(n-1)]

count = 0
if s <= w <= t:
    count += 1
for kg in a:
    w += kg
    if s <= w <= t:
        count += 1
print(count)

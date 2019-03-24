n = int(input())
k = int(input())
now = 1
for i in range(n):
    if now < k:
        now *= 2
    else:
        now += k
print(now)

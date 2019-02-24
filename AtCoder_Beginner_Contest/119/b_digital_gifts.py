n = int(input())
x_and_u = [input().split() for _ in range(n)]
sum = 0
for x,u in x_and_u:
    if u == 'JPY':
        sum += int(x)
    else:
        sum += 380000.0 * float(x)
print(sum)

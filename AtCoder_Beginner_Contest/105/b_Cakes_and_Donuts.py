n = int(input())
f = False
for i in range(n):
    for j in range(n):
        if 4*i+7*j == n:
            f = True
            break
print('Yes' if f else 'No')

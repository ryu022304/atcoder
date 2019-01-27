n = int(input())
a = list(input())
b = list(input())
c = list(input())

count = 0

for i in range(n):
    if a[i] == b[i] and b[i] == c[i]:
        continue
    elif a[i] == b[i] or b[i] == c[i] or a[i] == c[i]:
        count += 1
    else:
        count += 2

print(count)

n = int(input())
petals = map(int, input().split())

count = 0
for petal in petals:
    while True:
        if petal%2 == 0 or petal%3 == 2:
            petal -= 1
            count += 1
        else:
            break
print(count)

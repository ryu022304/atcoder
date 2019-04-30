n = int(input())
sum = 0
for i in range(1,10):
    for j in range(1,10):
        sum += i*j
res = sum - n
for i in range(1,10):
    for j in range(1,10):
        if i*j == res:
            print('{} x {}'.format(i,j))

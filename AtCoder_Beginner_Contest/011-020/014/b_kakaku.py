n,X = map(int, input().split())
a = [int(i) for i in input().split()]
X_bin = list(format(X,'0'+str(n)+'b'))
sum = 0
for i,b in enumerate(reversed(X_bin)):
    if b == '1':
        sum += a[i]
print(sum)

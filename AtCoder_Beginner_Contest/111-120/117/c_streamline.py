N,M = map(int, input().split())
X = [int(i) for i in input().split()]

X.sort()
print(X)

count = 0
if N > M:
    print(0)
else:
    for x in X:
        

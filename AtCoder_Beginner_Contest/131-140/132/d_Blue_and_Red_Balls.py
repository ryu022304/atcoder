import math
n,k = map(int,input().split())

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r)) if n-r >= 0 else 0

for i in range(1,k+1):
    red = n - k
    blue = i
    print(combinations_count(red+1,blue)*combinations_count(k-1,i-1)%(10**9+7))
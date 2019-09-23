k,x = map(int, input().split())
res = [str(i) for i in range(x-k+1, x+k)]
print(' '.join(res))
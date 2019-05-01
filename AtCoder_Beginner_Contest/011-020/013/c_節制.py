n,h = map(int,input().split())
a,b,c,d,e = map(int,input().split())

sum = 10**15

for i in range(n):
    y = (n*e - i*e - h - b*i)//(d+e)+1
    y = max(y, 0)
    if y <= n -i:
        sum = min(sum, a*i+c*y)
print(sum)

n = int(input())

def tri(n):
    a,b,c = 0,0,1
    for _ in [0]*n:
        a, b, c = b%10007, c%10007, (a+b+c)%10007
    return a

print(tri(n-1))

n = int(input())
a_list = list(map(int,input().split()))

def gcd(m,n):
    x = max(m,n)
    y = min(m,n)
    if y==0:
        return x
    else:
        while x%y!=0:
            x,y = y,x%y
        return y

res = []
l_gcd = [0]*(n+2)
r_gcd = [0]*(n+2)
for i in range(n+1):
    if i ==0:
        l_gcd[i] = 0
        r_gcd[n-i+1] = 0
        continue
    l_gcd[i] = gcd(l_gcd[i-1], a_list[i-1])
    r_gcd[n-i] = gcd(r_gcd[n-i+1], a_list[n-i])

for i in range(n+1):
    res.append(gcd(l_gcd[i],r_gcd[i+1]))

print(max(res))

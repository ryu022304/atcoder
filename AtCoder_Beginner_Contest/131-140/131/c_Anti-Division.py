a,b,c,d = map(int,input().split())

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

lcm_num = lcm(c,d)
c_num = (b//c - a//c) if a%c!=0 else (b//c - a//c + 1)
d_num = (b//d - a//d) if a%d!=0 else (b//d - a//d + 1)
ba_num = b//lcm_num - a//lcm_num if a%lcm_num!=0 else (b//lcm_num - a//lcm_num + 1)

print(c_num)
print(d_num)
print(ba_num)

if c == 1 or d == 1:
    print(0)
else:
    print(b-a+1-(c_num+d_num-ba_num) if b-a+1-(c_num+d_num-ba_num) > 0 else 0)

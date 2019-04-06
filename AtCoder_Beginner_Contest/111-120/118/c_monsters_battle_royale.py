n = int(input())
a = [int(i) for i in input().split()]

def func_gcd(a,b):
    if b == 0:
        return a
    else:
        return func_gcd(b,a%b)

if len(a) == 1:
    print(a[0])
else:
    res = func_gcd(a[0],a[1])
    for i in range(2,n):
        res = func_gcd(res,a[i])
    print(res)


'''
if len(a) == 1:
    print(a[0])
else:
    list_a = [max([mons%i for i in a]) for mons in a]
    print(list_a)
    list_b = [min([m%i for i in list_a if i != m and i!=0]) for m in list_a]
    print(list_b)
    print(min([i for i in list_b if i != 0]))
'''

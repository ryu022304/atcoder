n,a,b = map(int, input().split())
min_num = 0
max_num = 0

if a == n or b == n:
    min_num = min(a,b)
    max_num = min(a,b)
elif a == b and a == n:
    min_num = n
    max_num = n
elif a == 0 or b == 0:
    pass
elif n >= a + b:
    max_num = min(a,b)
elif n < a + b:
    min_num = abs(n-a-b)
    max_num = min(a,b)

print(max_num, min_num)
'''
n,a,b = map(int, input().split())

max_num = min(a,b)
min_num = max(a+b-n,0)

print(max_num, min_num)
'''

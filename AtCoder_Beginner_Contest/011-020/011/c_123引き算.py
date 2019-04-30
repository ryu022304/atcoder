n = int(input())
ng_list = [int(input()) for _ in range(3)]

for i in range(100):
    if n in ng_list:
        break
    if n >= 3 and n-3 not in ng_list:
        n -= 3
    elif n >= 2 and n-2 not in ng_list:
        n -= 2
    elif n >= 1 and n-1 not in ng_list:
        n -= 1
    else:
        break
print('YES' if n==0 else 'NO')

a,b,x = map(int,input().split())
if a > x:
    print('NO')
else:
    if a+b-x>=0:
        print('YES')
    else:
        print('NO')

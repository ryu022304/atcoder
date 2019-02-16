x = input()
if len(x.replace('ch','').replace('o','').replace('k','').replace('u','')) == 0:
    print('YES')
else:
    print('NO')

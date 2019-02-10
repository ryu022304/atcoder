path = []
for _ in [0]*3:
    path.extend(input().split())

if path.count('1') == 3 or path.count('2') == 3 or path.count('3') == 3 or path.count('4') == 3:
    print('NO')
else:
    print('YES')

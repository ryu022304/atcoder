s_list = list(input())
num = 15 - len(s_list)
if num + s_list.count('o') >= 8:
    print('YES')
else:
    print('NO')
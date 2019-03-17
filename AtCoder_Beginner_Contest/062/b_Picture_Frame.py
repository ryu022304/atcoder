h,w = map(int, input().split())
a_list = [list(input()) for _ in range(h)]

for a in a_list:
    a.insert(0,'#')
    a.append('#')
a_list.insert(0,['#']*(w+2))
a_list.append(['#']*(w+2))

for a in a_list:
    print(''.join(a))

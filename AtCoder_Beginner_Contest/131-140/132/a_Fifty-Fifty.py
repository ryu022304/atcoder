s_list = list(input())
s_set = set(s_list)

if len(s_set) == 2:
    if ''.join(s_list).count(s_list[0]) == 2 and ''.join(s_list).count(s_list[1]) == 2:
        print('Yes')
    else:
        print('No')
else:
    print('No')

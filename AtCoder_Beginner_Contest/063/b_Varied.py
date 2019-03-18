s = list(input())
s_len = len(s)
s_set = len(set(s))
if s_len == s_set:
    print('yes')
else:
    print('no')

s_list = list(input())
t_list = list(input())
if sorted(''.join(s_list)) < sorted(''.join(t_list),reverse=True):
    print('Yes')
else:
    print('No')

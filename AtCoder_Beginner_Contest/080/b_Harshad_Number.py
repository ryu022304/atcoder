n_list = list(input())
n_sum = sum(list(map(int,n_list)))
if int(''.join(n_list))%n_sum == 0:
    print('Yes')
else:
    print('No')

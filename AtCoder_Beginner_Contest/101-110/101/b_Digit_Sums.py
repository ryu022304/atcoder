n = int(input())
n_str = sum(list(map(int,list(str(n)))))
if n%n_str == 0:
    print('Yes')
else:
    print('No')

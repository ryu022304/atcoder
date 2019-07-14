n,m = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.sort()
if n >= m:
    print(0)
else:
    l_list = [x_list[i]-x_list[i-1] for i in range(1,m)]
    l_list.sort()
    print(sum(l_list[:m-n]))
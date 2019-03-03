import copy
n = int(input())
times = [int(i) for i in input().split()]
m = int(input())
px = [input().split() for _ in range(m)]
n_times = copy.copy(times)
for p,x in px:
    n_times[int(p)-1] = int(x)
    print(sum(n_times))
    n_times = copy.copy(times)

n = int(input())
cost_list = list(set([int(input()) for _ in [0]*n]))
cost_list.sort(reverse=True)
print(cost_list[1])

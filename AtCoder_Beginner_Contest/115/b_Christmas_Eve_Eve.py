n = int(input())
p_list = [int(input()) for _ in range(n)]
p_list = sorted(p_list)
print(p_list.pop(-1)//2 + sum(p_list))

num_list = sorted(list(map(int, input().split())))
k = int(input())
num_max = num_list.pop()
num_max = (2**k)*num_max
print(sum(num_list)+num_max)

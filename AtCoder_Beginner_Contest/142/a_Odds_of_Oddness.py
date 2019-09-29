n = int(input())
num_list = list(range(1,n+1))
odd_list = num_list[::2]
print(len(odd_list)/n)
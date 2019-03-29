n = int(input())
a_list = sorted(list(map(int,input().split())),reverse=True)
print(sum(a_list[::2])-sum(a_list[1::2]))

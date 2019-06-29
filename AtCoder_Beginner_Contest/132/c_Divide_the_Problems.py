n = int(input())
d_list = list(map(int,input().split()))
d_list.sort()
print(d_list[n//2]-d_list[n//2-1])
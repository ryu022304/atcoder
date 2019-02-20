l,h = map(int,input().split())
n = int(input())
a_list = [int(input()) for _ in range(n)]

for a in a_list:
    if l <= a <= h:
        print(0)
    elif a < l:
        print(l-a)
    else:
        print(-1)

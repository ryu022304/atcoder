n = int(input())
a_s = list(map(int,input().split()))
a_max = sorted(a_s)[-1]
a_min = sorted(a_s)[0]
print(a_max-a_min)

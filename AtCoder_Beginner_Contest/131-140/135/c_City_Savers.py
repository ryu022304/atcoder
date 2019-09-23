n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

res = 0
for i, b in enumerate(b_list):
    res += min(a_list[i], b)
    res += min(a_list[i+1], b-min(a_list[i],b))
    a_list[i+1] -= min(b-min(a_list[i],b), a_list[i+1])
print(res)
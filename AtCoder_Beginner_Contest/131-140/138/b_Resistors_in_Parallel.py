n = int(input())
a_list = list(map(int, input().split()))
res = []
for a in a_list:
    res.append(1/a)
print(1/sum(res))
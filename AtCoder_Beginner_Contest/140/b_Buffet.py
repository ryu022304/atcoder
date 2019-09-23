n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
c_list = list(map(int,input().split()))

res = sum(b_list)

for i in range(n-1):
    if a_list[i+1]-a_list[i]==1:
        res += c_list[a_list[i]-1]
print(res)
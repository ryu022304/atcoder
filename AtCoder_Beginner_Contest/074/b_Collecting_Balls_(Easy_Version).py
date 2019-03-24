n = int(input())
k = int(input())
x_list = list(map(int, input().split()))
count = 0
for x in x_list:
    count += min(x,abs(k-x))*2
print(count)

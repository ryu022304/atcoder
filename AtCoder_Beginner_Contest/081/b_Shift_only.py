n = int(input())
a_list = list(map(int, input().split()))

count_list = []
for a in a_list:
    count = 0
    q,mod = divmod(a,2)
    while True:
        if mod != 0:
            break
        else:
            q,mod = divmod(q,2)
            count += 1
    count_list.append(count)
print(min(count_list))

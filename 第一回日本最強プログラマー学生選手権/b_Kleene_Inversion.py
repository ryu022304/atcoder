n,k = map(int,input().split())
a_list = list(map(int,input().split()))
a_list_k = a_list*k
count = 0
for i in range(len(a_list_k)):
    for j in range(i,len(a_list_k)):
        if a_list_k[i] > a_list_k[j]:
            count += 1
print(count)

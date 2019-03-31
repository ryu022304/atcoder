x = int(input())
res_list = []
for i in range(1,x+1):
    if (i**0.5).is_integer():
        res_list.append(i)
print(max(res_list))

x = int(input())
res_list = [1]
for b in range(1,x+1):
    for p in range(2,x+1):
        if b**p <= x:
            res_list.append(b**p)
        else:
            break
print(max(res_list))

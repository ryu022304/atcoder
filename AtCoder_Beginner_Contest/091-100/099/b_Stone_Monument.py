a,b = map(int,input().split())
tmp_list = [0]*1000
tmp_list[0] = 1
for i in range(1,len(tmp_list)-1):
    tmp_list[i] = tmp_list[i-1]+i+1
tmp_list.pop(-1)
res_w = tmp_list[b-a-2]
res_e = tmp_list[b-a-1]
print(res_w-a)

from itertools import chain
n,m = map(int,input().split())
ab_list = [list(map(int, input().split())) for _ in range(m)]
tmp_list = sorted(list(chain(*ab_list)))
tmp_dic = {}
for i in range(1,n+1):
    tmp_dic[i]=0
for val in tmp_list:
    tmp_dic[val] += 1
for k,v in tmp_dic.items():
    print(v)

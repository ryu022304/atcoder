n,q = map(int, input().split())
s = list(input())
lr_list = [list(map(int,input().split())) for _ in range(q)]

ac_list = [1 if ''.join(s[i:i+2]) == 'AC' else 0 for i in range(len(s))]
print(ac_list)
for l,r in lr_list:
    #tmp_str = ''.join(s[l-1:r])
    #print(tmp_str.count('AC'))
    print(sum(ac_list[l-1:r-1]))

n,l = map(int,input().split())
taste_list = list(map(lambda x:l+x-1, list(range(1,n+1))))
pre_sum = sum(taste_list)

min_sum = 10000000
n_taste_list = list(map(abs, taste_list))

for i in taste_list:
    if abs(min_sum) > abs(i):
        min_sum = i

print(sum(taste_list)-min_sum)
#print(max(sum(taste_list)-min(n_taste_list), sum(taste_list)+min(n_taste_list)))
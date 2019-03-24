s_list = list(input())
str_list = ['A','C','G','T']
now_max = 0
for i,s in enumerate(s_list):
    if s in str_list:
        l = 1
        for next in s_list[i+1:]:
            #print(next)
            if next in str_list:
                l += 1
            else:
                break
        now_max = max(l,now_max)
print(now_max)

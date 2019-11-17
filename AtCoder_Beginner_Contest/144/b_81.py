n = int(input())
num_list = [2,3,4,5,6,7,8,9]
div_flag = False
for num in num_list:
    if n / num < 10 and int(n/num)==n/num:
        div_flag = True
if div_flag or (n==1):
    print('Yes')
else:
    print('No')
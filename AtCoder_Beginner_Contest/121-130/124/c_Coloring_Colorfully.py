s = list(input())
one_zero_list = ['0' if i%2==0 else '1' for i in range(len(s))]
zero_one_list = ['1' if i%2==0 else '0' for i in range(len(s))]

count_one_zero = len([0 for i in range(len(s)) if s[i]!=one_zero_list[i]])
count_zero_one = len([0 for i in range(len(s)) if s[i]!=zero_one_list[i]])

print(min(count_one_zero,count_zero_one))

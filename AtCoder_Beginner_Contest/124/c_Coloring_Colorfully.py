import math
s = input()
zero_one = s.count('01')
one_zero = s.count('10')
zero_zero = s.count('00')
one_one = s.count('11')
base = len(s)//2

if one_zero==base and zero_one==base:
    print(0)

import math
a,b = map(int, input().split())
print(math.ceil((b-1)/(a-1)))
"""
tmp = 1
count = 0
while tmp < b:
    tmp -= 1
    tmp += a
    count += 1
print(count)
"""
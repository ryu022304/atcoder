import math
n = int(input())
a = [int(i) for i in input().split() if int(i) != 0]
print(math.ceil(sum(a)/len(a)))

n = int(input())
s_list = list(input())
x = 0
res = 0
for s in s_list:
    if s == 'I':
        x += 1
    elif s == 'D':
        x -= 1
    res = max(res,x)
print(res)

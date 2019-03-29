a,b = map(int, input().split())
count = 0
for i in range(a,b+1):
    num = list(str(i))
    if num[0]==num[-1] and num[1]==num[-2]:
        count += 1
print(count)

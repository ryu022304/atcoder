n = int(input())
count = 0
for i in range(1,n+1):
    i_s = str(i)
    if len(i_s)%2 == 1:
        count += 1
print(count)
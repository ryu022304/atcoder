a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
x = int(input())
count = 0
for a in range(a_500+1):
    for b in range(b_100+1):
        c_num = int((x-a*500-b*100)/50)
        if c_num in range(c_50+1):
            count += 1
print(count)

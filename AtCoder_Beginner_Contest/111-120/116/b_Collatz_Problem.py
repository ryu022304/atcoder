s = int(input())
a_list = [s]
prev_num = 1
for i in range(1,1000001):
    n = a_list[i-1]
    if n%2 == 0:
        a_list.append(n//2)
    else:
        a_list.append(3*n+1)
    if prev_num == len(set(a_list)):
        print(i+1)
        break
    else:
        prev_num = len(set(a_list))

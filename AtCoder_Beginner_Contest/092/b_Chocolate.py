n = int(input())
d,x = map(int,input().split())
a_list = [int(input()) for _ in range(n)]
count_list = []
for a in a_list:
    count_list.append(1+(d-1)//a)
print(sum(count_list)+x)

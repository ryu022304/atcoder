n = int(input())
a_list = list(map(int,input().split()))
tmp_list = []
for a in a_list:
    while a%2==0:
        a //= 2
    tmp_list.append(a)
print(len(set(tmp_list)))

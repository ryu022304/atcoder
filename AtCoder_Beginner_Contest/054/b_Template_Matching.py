n,m = map(int,input().split())
a_list = [input() for _ in range(n)]
b_list = [input() for _ in range(m)]
count = 0
print(a_list)
print(b_list)
for i,b in enumerate(b_list):
    for j,a in enumerate(a_list):
        

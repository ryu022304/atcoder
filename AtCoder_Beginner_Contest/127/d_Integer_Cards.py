N, M = map(int, input().split())
A = list(map(int, input().split()))
p = [(A[i], 1) for i in range(N)]
for j in range(M):
    B, C = map(int, input().split())
    p.append((C, B))
p.sort()
p.reverse()
ans, cnt = 0, N
for (v, c) in p:
    use = min(c, cnt)
    ans += use * v
    cnt -= use
print(ans)

'''
n,m = map(int,input().split())
a_list = list(map(int,input().split()))
bc_list = [list(map(int,input().split())) for _ in range(m)]

d_list = []
for b,c in bc_list:
    d_list.extend([c]*b)
d_list = sorted(d_list,reverse=True)[:n]

a_list = sorted(a_list)

print(a_list)
print(d_list)
for i,d in enumerate(d_list):
    if a_list[i] < d:
        a_list[i] = d
    else:
        break

print(sum(a_list))

for b,c in bc_list:
    a_list = sorted(a_list)
    for i,a in enumerate(a_list[:b]):
        if a < c:
            a_list[i] = c

print(a_list)
print(sum(a_list))
'''
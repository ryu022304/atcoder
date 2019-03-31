n,q = map(int,input().split())
s = list(input())
td_list = [input().split() for _ in range(q)]
cells = [0]*2*10**5
cell_dic = {}
for i in range(n):
    cells[i] = 1
for c in s:
    cell_dic[c] = [i for i, x in enumerate(s) if x == c]

for t,d in td_list:
    if t not in cell_dic:
        continue
    indexes = cell_dic[t]
    if d == 'R':
        indexes = sorted(indexes,reverse=True)
    for i in indexes:
        if d == 'R':
            if i == len(s)-1:
                cells[i] = 0
                continue
            if cells[i] != 0:
                cells[i+1] += cells[i]
                cells[i] = 0
        elif d == 'L':
            if i == 0:
                cells[i] = 0
                continue
            if cells[i] != 0:
                cells[i-1] += cells[i]
                cells[i] = 0
        print(indexes)
        print(i,t,d)
        print(cells[:10])

print(cells[:10])
print(sum(cells))

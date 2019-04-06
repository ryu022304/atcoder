n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
abc = [a,b,c]
count = 0
if a in l:
    l.remove(a)
    abc.remove(a)
if b in l:
    l.remove(b)
    abc.remove(b)
if c in l:
    l.remove(c)
    abc.remove(c)

for alp in abc:
    count_list = [abs(alp-take) for take in l if abs(alp-take) <= 10]
    print(count_list)

    count += min(count_list)
print(count)
print(l)
print(abc)

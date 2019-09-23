s = list(input())
pre = ''
f = False
for i in s:
    if i == pre:
        f = True
    pre = i

print('Bad' if f else 'Good')
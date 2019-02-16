n = int(input())
s = input()
f = False

for i in range(n):
    if i == 0:
        str = 'b'
    elif i%3 == 0:
        str = ('b'+str+'b')
    elif i%3 == 1:
        str = ('a'+str+'c')
    elif i%3 == 2:
        str = ('c'+str+'a')
    if str == s:
        f = True
        break
if f:
    print(i)
else:
    print(-1)

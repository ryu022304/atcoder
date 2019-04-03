s = list(input())
t = list(input())
f = False
for _ in range(len(s)):
    head = s.pop(-1)
    s.insert(0,head)
    if s == t:
        f = True

print('Yes' if f else 'No')

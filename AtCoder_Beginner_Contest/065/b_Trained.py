n = int(input())
a_s = [int(input()) for _ in range(n)]
button = 1
count = 0
for _ in range(len(a_s)):
    button = a_s[button-1]
    count += 1
    if button == 2:
        print(count)
        break
if count == len(a_s):
    print(-1)

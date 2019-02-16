s = list(input())

count = 1
res = ''
for i in range(len(s)):
    if i == len(s)-1:
        res += (s[i]+str(count))
        break
    if s[i] == s[i+1]:
        count += 1
    else:
        res += (s[i]+str(count))
        count = 1
print(res)

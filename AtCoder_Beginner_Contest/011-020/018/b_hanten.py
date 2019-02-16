s = input()
n = int(input())
for _ in [0]*n:
    l,r = map(int,input().split())
    temp_s = s[:l-1]+s[l-1:r][::-1]+s[r:]
    s = temp_s
print(s)

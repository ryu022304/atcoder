n = int(input())
s_list = [input() for _ in range(n)]
res_ab = 0
res_ba = 0
res_a = 0
res_b = 0
for s in s_list:
    res_ab += s.count('AB')
    if s[0]=='B' and s[-1]=='A':
        res_ba += 1
    elif s[0]=='B':
        res_a += 1
    elif s[-1] == 'A':
        res_b += 1

if res_ba == 0:
    print(res_ab+min(res_a,res_b))
else:
    if res_a+res_b > 0:
        print(res_ab+res_ba+min(res_a,res_b))
    else:
        print(res_ab+res_ba-1)

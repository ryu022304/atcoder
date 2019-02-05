s_list = list(input())
t_list = list(input())

words = ['a', 't', 'c', 'o', 'd', 'e', 'r']

count = 0
for i in range(len(s_list)):
    if s_list[i] == t_list[i]:
        count += 1
        continue
    elif s_list[i] == '@':
        if t_list[i] in words:
            count += 1
    elif t_list[i] == '@':
        if s_list[i] in words:
            count += 1

if count == len(s_list):
    print('You can win')
else:
    print('You will lose')

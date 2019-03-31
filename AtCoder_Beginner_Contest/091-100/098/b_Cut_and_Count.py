n = int(input())
s = input()
count_list = []
for i in range(1,n):
    count = 0
    left_list = set(s[:i])
    right_list = set(s[i:])
    for moji in left_list:
        if moji in right_list:
            count += 1
    count_list.append(count)
print(max(count_list))

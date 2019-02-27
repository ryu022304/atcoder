s = input()
k = int(input())
passwd_list = []
if len(s) < k:
    print(0)
else:
    for i in range(len(s)):
        passwd_list.append(s[i:i+k])
    tmp_passwd_list = [i for i in passwd_list if len(i)==k]
    print(len(set(tmp_passwd_list)))

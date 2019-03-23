s = list(input())
alphabet_list = [chr(i) for i in range(97,97+26)]
for sl in s:
    if sl in alphabet_list:
        alphabet_list.remove(sl)
    else:
        pass
if len(alphabet_list) == 0:
    print('None')
else:
    print(alphabet_list[0])

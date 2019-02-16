s = list(input())
n = int(input())
moji_list = []
for str in s:
    for strs in s:
        moji = str+strs
        if moji not in moji_list:
            moji_list.append(moji)
print(moji_list[n-1])

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
pre_one,one = n,n
pre_two,two = 0,0
pre_three,three = 0,0
pre_four,four = 0,0
pre_five,five = 0,0
six = 0
i = 1
while six < n:
    if pre_one > 0:
        if one < a:
            two += pre_one
            one = 0
        else:
            one -= a
            two += a
    if pre_two > 0:
        if two < b:
            three += pre_two
            two = 0
        else:
            two -= b
            three += b
    if pre_three > 0:
        if three < c:
            four += pre_three
            three = 0
        else:
            three -= c
            four += c
    if pre_four > 0:
        if four < d:
            five += four
            four = 0
        else:
            four -= d
            five += d
    if pre_five > 0:
        if five < e:
            six += five
            five = 0
        else:
            five -= e
            six += e
    print(one,two,three,four,five,six)
    if six >= n:
        print(i)
        break
    if i >= 10:
        print('end')
        break
    i += 1
    pre_one = one
    pre_two = two
    pre_three = three
    pre_four = four
    pre_five = five

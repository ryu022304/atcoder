num_list = [int(input()) for _ in range(5)]
res = []
zero = []
one = []
two = []
three = []
four = []
five = []
for n in num_list:
    if n%10 > 5:
        res.append(n)
for n in num_list:
    if n%10 == 0:
        zero.append(n)
    elif n%10 == 1:
        one.append(n)
    elif n%10 == 2:
        two.append(n)
    elif n%10 == 3:
        three.append(n)
    elif n%10 == 4:
        four.append(n)
    elif n%10 == 5:
        five.append(n)
sum = 0
res.extend(zero)
res.extend(five)
res.extend(four)
res.extend(three)
res.extend(two)
res.extend(one)
for i,v in enumerate(res):
    plus = 0
    if v%10==0:
        pass
    else:
        plus = 10-v%10
    if i == 4:
        sum += v
        break
    else:
        sum += v + plus
print(sum)

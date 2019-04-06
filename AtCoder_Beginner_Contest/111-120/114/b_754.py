x = input()
res = []
for i in range(len(x)-2):
    res.append(abs(int(x[i:i+3])-753))
print(min(res))

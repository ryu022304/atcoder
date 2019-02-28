sa = list(input())
sb = list(input())
sc = list(input())
dic = {'a':sa,'b':sb,'c':sc}
res = 'a'
for _ in range(len(sa+sb+sc)):
    if len(dic[res])==0:
        print(res.upper())
        break
    res = dic[res].pop(0)

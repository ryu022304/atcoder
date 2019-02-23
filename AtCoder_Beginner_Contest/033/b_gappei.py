n = int(input())
towns_and_people = [input().split() for _ in range(n)]
people_half = sum([int(i[1]) for i in towns_and_people])//2
flag = False
for t,p in towns_and_people:
    if int(p) > people_half:
        print(t)
        flag = True
        break
if not flag:
    print('atcoder')

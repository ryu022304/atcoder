import collections
n = int(input())
people = [input() for _ in [0]*n]
c = collections.Counter(people)
ans = c.most_common()
print(ans[0][0])

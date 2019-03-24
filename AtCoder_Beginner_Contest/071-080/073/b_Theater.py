n = int(input())
seats = [list(map(int, input().split())) for _ in range(n)]
count = 0
for l,r in seats:
    count += (r-l+1)
print(count)

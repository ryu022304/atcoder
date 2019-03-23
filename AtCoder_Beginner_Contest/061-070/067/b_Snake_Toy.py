n,k = map(int, input().split())
l_list = list(map(int, input().split()))
print(sum(sorted(l_list)[-k:]))

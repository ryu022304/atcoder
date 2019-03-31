n,m,x = map(int,input().split())
a_list = list(map(int,input().split()))
tmp_list = [1  if i in a_list else 0 for i in range(n+1)]
print(min(sum(tmp_list[:x]),sum(tmp_list[x:])))

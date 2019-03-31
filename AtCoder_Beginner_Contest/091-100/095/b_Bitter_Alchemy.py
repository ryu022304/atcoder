n,x = map(int, input().split())
m_list = [int(input()) for _ in range(n)]
donuts_sum = sum(m_list)
print(n+(x-donuts_sum)//min(m_list))

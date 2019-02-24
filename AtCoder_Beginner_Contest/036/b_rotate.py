import numpy as np
n = int(input())
s_matrix = [list(input()) for _ in range(n)]
res_array = np.rot90(s_matrix,-1)
for ar in res_array:
    print(''.join(ar))

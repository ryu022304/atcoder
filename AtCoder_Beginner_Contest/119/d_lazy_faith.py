import numpy as np
a,b,q = map(int,input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
s_and_t = s+t

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]
print('------------')
for pos in x:
    count = 0
    first = getNearestValue(s_and_t,pos)
    count += abs(pos - first)
    if first in s:
        second = getNearestValue(t,first)
    elif first in t:
        second = getNearestValue(s,first)
    count += abs(first - second)
    print('pos:'+str(pos))
    print('first:'+str(first))
    print('second:'+str(second))
    print(count)

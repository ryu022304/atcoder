n = int(input())
w_list = [input() for _ in range(n)]
if len(w_list) != len(set(w_list)):
    print('No')
else:
    f = True
    tail = w_list[0][0]
    for w in w_list:
        if w[0] != tail:
            f = False
        else:
            tail = w[-1]
            pass
    print('Yes' if f else 'No')

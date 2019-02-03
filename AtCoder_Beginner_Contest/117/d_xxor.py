N,K = map(int, input().split())
A = [int(i) for i in input().split()]
sum_list = []
K_bit_len = len(bin(K))-2
if K == 0:
    sum_list.append(A[0])
else:
    for i in range(K+1):
        sum = 0
        i_bin = str(bin(i)[2:]).zfill(K_bit_len)
        if i_bin[0] != '1':
            continue
        for a in A:
            a_bin = str(bin(a)[2:]).zfill(K_bit_len)
            sum += int(i ^ a)
        sum_list.append(sum)

print(max(sum_list))

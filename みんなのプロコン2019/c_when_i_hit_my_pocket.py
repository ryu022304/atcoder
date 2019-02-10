K, A, B = map(int, input().split())

biscuit = 1
yen = 0

def exchange_a(a):
    global biscuit, yen
    yen += 1
    biscuit -= a

def exchange_b(b):
    global biscuit, yen
    yen -= 1
    biscuit += b

for _ in [0]*K:
    if B-A >1:
        if yen > 0:
            exchange_b(B)
        elif biscuit == A:
            exchange_a(A)
        else:
            biscuit += 1
    else:
        biscuit += 1
    #print('bis:'+str(biscuit))
    #print('yen:'+str(yen))
    #print()

print(biscuit)

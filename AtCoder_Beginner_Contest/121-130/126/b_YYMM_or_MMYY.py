s = list(input())
left = int(''.join(s[:2]))
right = int(''.join(s[2:]))
lyy = False
lmm = False
ryy = False
rmm = False
if 0 <= left <= 99:
    lyy = True
    if 1<= left <= 12:
        lmm = True

if 0 <= right <= 99:
    ryy = True
    if 1<= right <= 12:
        rmm = True

if lyy and lmm and ryy and rmm:
    print('AMBIGUOUS')
elif lyy and rmm:
    print('YYMM')
elif lmm and ryy:
    print('MMYY')
else:
    print('NA')
m = int(input())

if m <= 100:
    print("{0:02d}".format(0))
elif 100 <= m and m <= 5000:
    print("{0:02d}".format(int(m/1000*10)))
elif 6000 <= m and m <= 30000:
    print("{0:02d}".format(int(m/1000)+50))
elif 35000 <= m and m <= 70000:
    res = int((m/1000-30)/5+80)
    print("{0:02d}".format(res))
elif 70000 < m:
    print("{0:02d}".format(89))

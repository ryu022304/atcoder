w,a,b = map(int, input().split())
if a < b:
    if a + w > b:
        print(0)
    else:
        print(abs(a+w-b))
else:
    if b + w > a:
        print(0)
    else:
        print(abs(b+w-a))

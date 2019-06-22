w,h,x,y = map(int,input().split())
res = w * h / 2

if (w==1) or (h==1):
    print(res, 0)
else:
    if (x==(w//2)) and (y==(h//2)) and w%2==0 and h%2==0:
        print(res, 1)
    else:
        print(res, 0)

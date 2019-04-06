x1,y1,x2,y2 = map(int, input().split())
w = x2-x1
h = y2-y1
print(x2-h,y2+w,x1-h,y1+w)

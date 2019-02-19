n,m = map(int,input().split())
hour = 360/(12*60)
min = 360/60
pos_h = (n%12*60+m)*hour
pos_m = min*m
num_list = sorted([abs(pos_h - pos_m),360-abs(pos_h - pos_m)])
print(num_list[0])

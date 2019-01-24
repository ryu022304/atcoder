import math
d,w=(int(i) for i in input().split())
dir = ''
d /= 10
if 11.25 <= d < 33.75:
    dir = 'NNE'
elif 33.75 <= d < 56.25:
    dir = 'NE'
elif 56.25 <= d < 78.75:
    dir = 'ENE'
elif 78.75 <= d < 101.25:
    dir = 'E'
elif 101.25 <= d < 123.75:
    dir = 'ESE'
elif 123.75 <= d < 146.25:
    dir = 'SE'
elif 146.25 <= d < 168.75:
    dir = 'SSE'
elif 168.75 <= d < 191.25:
    dir = 'S'
elif 191.25 <= d < 213.75:
    dir = 'SSW'
elif 213.75 <= d < 236.25:
    dir = 'SW'
elif 236.25 <= d < 258.75:
    dir = 'WSW'
elif 258.75 <= d < 281.25:
    dir = 'W'
elif 281.25 <= d < 303.75:
    dir = 'WNW'
elif 303.75 <= d < 326.25:
    dir = 'NW'
elif 326.25 <= d < 348.75:
    dir = 'NNW'
else:
    dir = 'N'

def my_round(x,d=0):
    p=10**d
    return (x*p*2+1)//2/p

wp = my_round(w/60,1)

wp2 = 0
if 0.0 <= wp <= 0.2:
    wp2 = 0
elif 0.3 <= wp <= 1.5:
    wp2 = 1
elif 1.6 <= wp <= 3.3:
    wp2 = 2
elif 3.4 <= wp <= 5.4:
    wp2 = 3
elif 5.5 <= wp <= 7.9:
    wp2 = 4
elif 8.0 <= wp <= 10.7:
    wp2 = 5
elif 10.8 <= wp <= 13.8:
    wp2 = 6
elif 13.9 <= wp <= 17.1:
    wp2 = 7
elif 17.2 <= wp <= 20.7:
    wp2 = 8
elif 20.8 <= wp <= 24.4:
    wp2 = 9
elif 24.5 <= wp <= 28.4:
    wp2 = 10
elif 28.5 <= wp <= 32.6:
    wp2 = 11
elif 32.7 <= wp:
    wp2 = 12

if wp2 == 0:
    print('C',0)
else:
    print(dir,wp2)

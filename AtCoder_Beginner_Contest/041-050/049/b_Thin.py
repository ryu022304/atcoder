h,w = map(int,input().split())
pixels = [input() for _ in range(h)]
n_pixel = []
for p in pixels:
    n_pixel.append(p)
    n_pixel.append(p)

for np in n_pixel:
    print(''.join(np))

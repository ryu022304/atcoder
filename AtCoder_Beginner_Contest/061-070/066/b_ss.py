s_origin = input()
s_copy = s_origin[:]
for _ in range(len(s_origin)):
    s_copy = s_copy[:-1]
    if len(s_copy)%2 == 1:
        continue
    else:
        s_left = s_copy[:int(len(s_copy)/2)]
        s_right = s_copy[int(len(s_copy)/2):]
        if s_left == s_right:
            print(len(s_copy))
            break

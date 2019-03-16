s_list = list(input())
a_num = 0
z_num = 0
for i,a in enumerate(s_list):
    if a == 'A':
        a_num = i
        break
rs_list = reversed(s_list)
for j,z in enumerate(rs_list):
    if z == 'Z':
        z_num = j
        break
if z_num == 0:
    print(len(s_list[a_num:]))
else:
    print(len(s_list[a_num:-z_num]))

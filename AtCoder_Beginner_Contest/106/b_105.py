n = int(input())
kisu_list = [i for i in range(1,n+1) if i%2==1]
count = 0
for kisu in kisu_list:
    yakusu = [i for i in range(1,kisu+1) if kisu%i==0]
    if len(yakusu)==8:
        count += 1
print(count)

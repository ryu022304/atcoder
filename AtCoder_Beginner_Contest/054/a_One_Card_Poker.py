a,b = map(int,input().split())
cards = [2,3,4,5,6,7,8,9,10,11,12,13,1]
a_card = cards.index(a)
b_card = cards.index(b)
if a_card > b_card:
    print('Alice')
elif a_card < b_card:
    print('Bob')
else:
    print('Draw')

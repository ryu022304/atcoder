rank = [int(input()) for _ in [0]*3]
rank_sorted = sorted(rank,reverse=True)
for r in rank:
    print(rank_sorted.index(r)+1)

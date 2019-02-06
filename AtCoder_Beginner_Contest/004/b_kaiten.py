board = []
for _ in [0]*4:
    board.append(input().split())

for line in board[::-1]:
    print(' '.join(line[::-1]))

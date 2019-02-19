n = int(input())
a = [int(input()) for _ in [0]*n]
print(len(a)-len(set(a)))

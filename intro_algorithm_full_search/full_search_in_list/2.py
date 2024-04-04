N, V = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for a in A:
    if a == V:
        cnt += 1
print(cnt)
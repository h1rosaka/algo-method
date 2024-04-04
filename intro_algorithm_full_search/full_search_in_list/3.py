N = int(input())
A = map(int, input().split())

cnt = 0
for a in A:
    if a > 0:
        cnt += 1

print(cnt)
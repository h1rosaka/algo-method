N = int(input())
P = [-1] + list(map(int, input().split()))

children = [[] for _ in range(N)]

for i in range(1,N):
    children[P[i]].append(i)

cnt = 0
for i in range(1,N):
    if len(children[i])==0:
        cnt += 1
print(cnt)
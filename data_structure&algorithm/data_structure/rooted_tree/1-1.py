N = int(input())
P = [0] + list(map(int, input().split()))


children = [[] for _ in range(N)]

for i in range(1,N):
    children[P[i]].append(i)

Q = int(input())
for _ in range(Q):
    v = int(input())

    print(*children[P[v]])
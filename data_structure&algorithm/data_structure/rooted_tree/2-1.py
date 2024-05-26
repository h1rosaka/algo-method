N = int(input())


parent = [-1 for _ in range(N)]
children = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    parent[b] = a
    children[a].append(b)


Q = int(input())

for _ in range(Q):
    v = int(input())

    parent_v = parent[v]


    print(*sorted(children[parent_v]))



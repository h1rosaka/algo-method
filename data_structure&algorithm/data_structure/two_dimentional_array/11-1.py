# TLE
H, W = map(int, input().split())
grid = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "#":
            grid[i][j] = 1
    
dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]


Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0]==0:
        p = query[1]
        q = query[2]
        for d in range(5):
            new_p = p + dx[d]
            new_q = q + dy[d]
            if 0 <= new_p < H and 0 <= new_q < W:
                grid[new_p][new_q] = 1 - grid[new_p][new_q]

    else:
        total = 0
        for i in range(H):
            total += sum(grid[i])
        print(total)
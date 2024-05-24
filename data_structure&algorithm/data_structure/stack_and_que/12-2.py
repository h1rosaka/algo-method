from collections import deque
H, W = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


board = []
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "S":
            sx, sy = i, j
        if s[j] == "G":
            gx, gy = i, j
    board.append(s)

check_places = deque([])
check_places.append([sx, sy])

dist = [[-1 for j in range(W)] for i in range(H)]
dist[sx][sy] = 0

while len(check_places)>0:
    x, y = check_places.popleft()
    # 周囲四ます
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0<=nx<H and 0<=ny<W and board[nx][ny]!="#" and dist[nx][ny]==-1:
            dist[nx][ny] = dist[x][y] + 1
            check_places.append([nx, ny])

print(dist[gx][gy])     
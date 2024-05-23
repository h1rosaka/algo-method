# 一部不正解
from collections import deque
H, W = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


board = []
for i in range(H):
    s = input()
    for j in range (W):
        if s[j] == "S":
            sx, sy = i,j
        if s[j] == "G":
            gx, gy = i,j
    board.append(s)

x, y = sx, sy
place_to_go = deque([])
dist = [[-1 for _ in range(W)] for _ in range(H)]
dist[x][y] = 0
place_to_go.append([sx,sy])

while [x, y] != [gx, gy]:
    
    x, y = place_to_go.popleft()


    # 隣接４マスに関して
    for i in range(4):
        nx , ny = x+dx[i], y+dy[i]
        
        # ボード内でかつ通路で、まだ踏んでない所なら、距離を計算
        if 0<=nx<H and 0<=ny<W and board[nx][ny] != "#" and dist[nx][ny]==-1:
            place_to_go.append([nx, ny])
            dist[nx][ny] = dist[x][y] + 1
            
          
print(dist[x][y])




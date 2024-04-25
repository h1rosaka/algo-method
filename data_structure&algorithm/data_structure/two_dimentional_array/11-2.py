H, W = map(int, input().split())

num_blacks = 0




grid = [[0 for j in range(W)] for i in range(H)]

# 初期状態の取得
# 行ごとにループ
for i in range(H):
    s = input()
    #カラムごとにループ
    for j in range(W):
        if s[j]=="#":
            grid[i][j] = 1
            num_blacks += 1


dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]

# クエリへの回答
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0]==0:
        p = query[1]
        q = query[2]
        for d in range(5):
            x = p + dx[d]
            y = q + dy[d]

            if 0 <= x < H and 0 <= y < W:
                if grid[x][y] == 1:
                    num_blacks -= 1
                else:
                    num_blacks += 1
                grid[x][y] = 1 - grid[x][y]
    else:
        print(num_blacks)
                 
        


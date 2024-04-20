H , W = map(int, input().split())

# リストのリストにする。
board_state = []
for _ in range(H):
    s = input()

    current_row = []
    for character in s:
        if character == ".":
            current_row.append(0)
        else:
            current_row.append(1)

    board_state.append(current_row)

dx = [0, 1, 0, -1, 0]
dy = [0, 0, 1, 0, -1]
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    p = query[1]
    q = query[2]

    if query[0] == 0:
        for d in range(5):
            target_x = p + dx[d]
            target_y = q + dy[d]
            if 0 <= target_x < H and 0 <= target_y < W:
                board_state[target_x][target_y]  =  1 - board_state[target_x][target_y]
    else:
        cnt = 0
        for d in range(5):
            target_x = p + dx[d]
            target_y = q + dy[d]
            if 0 <= target_x < H and 0 <= target_y < W:
                cnt += board_state[target_x][target_y]
        print(cnt)


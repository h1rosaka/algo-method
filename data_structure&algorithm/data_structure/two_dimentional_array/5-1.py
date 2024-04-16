H, W  = map(int, input().split())

s_list = []
for _ in range(H):
    s = input()
    s_list.append(s)

Q = int(input())


def check_horizontally(x,y):
    horizontal_cnt = 0
    if W == 1:
        pass
    else:
        if y == 0:
            if s_list[x][y+1] == "#":
                horizontal_cnt = 1
        elif y == W-1:
            if s_list[x][y-1] == "#":
                horizontal_cnt = 1
        else:
            if s_list[x][y+1] == "#":
                horizontal_cnt += 1
            if s_list[x][y-1] == "#":
                horizontal_cnt += 1
    return horizontal_cnt


def check_virtically(x,y):
    virtical_cnt = 0
    if H == 1:
        pass
    else:
        if x == 0:
            if s_list[x+1][y] == "#":
                virtical_cnt = 1
        elif x == H-1:

            if s_list[x-1][y] == "#":
                virtical_cnt = 1

        else:
            if s_list[x-1][y] == "#":
                virtical_cnt += 1
            if s_list[x+1][y] == "#":
                virtical_cnt += 1
    return virtical_cnt



# 0行目だけど元々0行しかなくて一個下の行がないとか 最後の行が

for _ in range(Q):
    x, y = map(int, input().split())

    num_bombs = check_horizontally(x,y) + check_virtically(x,y)
    print(num_bombs)
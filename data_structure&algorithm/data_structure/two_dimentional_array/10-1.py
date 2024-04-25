H, W = map(int, input().split())


num_of_black_in_this_row_bucket = [0 for _ in range(H)]
num_of_black_in_this_column_bucket = [0 for _ in range(W)]
board = []

# 行ごとにループ
for i in range(H):
    s = input()
    board.append(s)
    num_of_black_in_this_row = 0
    # 行の中で文字ごとにループ
    for j in range(W):
        if s[j] == "#":
            num_of_black_in_this_row += 1
            num_of_black_in_this_column_bucket[j] += 1

    num_of_black_in_this_row_bucket[i] = num_of_black_in_this_row


Q = int(input())

for _ in range(Q):
    p, q = map(int, input().split())
    
    total_base = num_of_black_in_this_row_bucket[p] + num_of_black_in_this_column_bucket[q]

    if board[p][q] == "#":
        total = total_base -1
    else:
        total = total_base
    print(total)



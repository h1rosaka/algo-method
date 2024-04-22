board_size, num_steps = map(int, input().split())


board = []

for _ in range(board_size):
    initial_state_of_this_row = []
    input_string = input()
    for cell in input_string:
        if cell == "#":
            initial_state_of_this_row.append(1)
        else:
            initial_state_of_this_row.append(0)

    board.append(initial_state_of_this_row)


dx = [-1, -1, -1,  0, 0,  1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]



def tell_me_x(i,j):
    x = 0
    for d in range(8):
        new_i = i + dx[d]
        new_j = j + dy[d]
        
        if 0<= new_i < board_size and 0 <= new_j < board_size:
            checking_cell = board[new_i][new_j]
            # print(new_i)
            # print(new_j)
            # if checking_cell == None:
            #     print(board)
            # print(checking_cell)
            x += checking_cell
    return x


def my_next_state(i,j):
    my_current_state = board[i][j]
    x = tell_me_x(i,j)

    my_next_state = my_current_state # 特別な条件がなければそのまま。
    if my_current_state == 0 and x ==3:
        my_next_state = 1
    if my_current_state == 1 and (x<=1 or 4<=x):
        my_next_state = 0
    return my_next_state

def go_to_next_step(board):
    new_board = []
    for i in range(board_size):
        current_row = board[i]
        new_current_row = []
        for j in range(board_size):
            new_state_of_cell = my_next_state(i,j)
            new_current_row.append(new_state_of_cell)
        new_board.append(new_current_row)
        # board = new_board
    return new_board



for i in range(num_steps):
    board = go_to_next_step(board)
    # print(i)
    # print(board)



for row in board:
    print("".join(["#" if item == 1 else "." for item in row]))
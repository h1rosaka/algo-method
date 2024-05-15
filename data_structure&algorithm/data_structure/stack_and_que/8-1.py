N = int(input())
A = list(map(int, input().split()))


# [i, j] i番目の日のスコアがjという配列をここに入れる
stack = []

stack.append([0,0])

for i in range(1,N):
    score = A[i]

    # 過去に自分以上のスコアがある場合、その日はもう選ばれないので消す
    while score <= stack[-1][1]:
        stack.pop()

    # スパンの計算
    span = i - stack[-1][0]
    print(span)

    # 本日のスコアを追加
    stack.append([i,score])



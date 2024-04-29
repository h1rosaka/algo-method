N, K = map(int, input().split())
S = input()

left = [-1 for _ in range(N)]
right = [-1 for _ in range(N)]

#初期値挿入
# 方向ごとの最初に出てくる未踏のマス
for i in range(N):
    if i != 0:
        left[i] = i - 1
    if i != N-1:
        right[i] = i + 1



direction = 1 # 右方向
v = K 
total_time = 0
while True:
    # vを踏み終えたマスにする(連結リストから今回のマスへの参照を外す)
    right[left[v]] = right[v]
    left[right[v]] = left[v]

    # 次の方向決定
    if S[v] == "<":
        direction = 0 
    elif S[v] == ">":
        direction = 1

    # 次のマスの確認
    if direction == 1:
        nv = right[v]
    else:
        nv = left[v]

    # 時間計算して移動
    total_time += abs(nv - v)
    v = nv
    if v == 0 or v == N-1:
        break 
print(total_time)

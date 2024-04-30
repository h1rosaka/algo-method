N, K = map(int, input().split())
S = input()

right = [-1 for _ in range(N)]
left = [-1 for _ in range(N)]

for i in range(N):
    if i != 0:
        left[i] = i-1
    if i != N-1:
        right[i] = i+1 # TODO確認


v = K
direction = 1 # 右
total_time = 0

while True:
    # 踏んだことにする
    left[right[v]] = left[v]
    right[left[v]] = right[v]

    # 次のマス
    if direction == 1:
        nv = right[v]
    else:
        nv = left[v]

    # 次の方向を確認しておく
    if S[nv] == ">":
        direction = 1
    elif S[nv] == "<":
        direction = -1

    # 移動時間計算して移動
    total_time += abs(v-nv)
    v = nv

    if v == 0 or v == N-1:
        break

print(total_time)
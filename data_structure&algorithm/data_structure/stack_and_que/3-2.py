N, Q = map(int, input().split())

# 最大N個入るキュー　
que = [-1 for _ in range(N)]

head = 0
tail = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        v = query[1]
        que[tail] = v
        tail += 1
        if tail == N:
            tail = 0

    else:
        que[head] = -1
        head += 1
        if head == N:
            head = 0

for i in range(N):
    print(que[i])
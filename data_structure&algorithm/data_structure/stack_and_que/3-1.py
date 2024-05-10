N, Q = map(int, input().split())

A = [-1 for _ in range(N)]
head = 0
tail = 0


for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        v = query[1]
        A[tail] = v
        tail += 1
        if tail == N:
            tail = 0

    else:
        A[head] = -1
        head += 1
        if head == N:
            head = 0

for i in range(N):
    print(A[i])


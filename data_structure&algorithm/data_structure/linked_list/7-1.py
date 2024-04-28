N = int(input())
A = list(map(int, input().split()))
Q = int(input())


# 自分のエントリー番号を索引に、前/後の人のエントリー番号を返す
front = [-1 for i in range(N)]
back = [-1 for i in range(N)]

for i in range(N):
    entry_num = A[i]
    if i != 0:
        front[entry_num] = A[i-1]
    if i != N-1:
        back[entry_num] = A[i+1]



for _ in range(Q):
    querytype, v = map(int, input().split())

    if querytype == 0:
        if front[v] == -1:
            print("Error")
        else:
            nv = front[v]
            print(nv)

            back[nv] = back[v]
            front[v] = front[nv]
            if front[nv] != -1:
                back[front[nv]] = v
            if back[v] != -1:
                front[back[v]] = nv
            back[v] = nv
            front[nv] = v
    else:
        back[front[v]] = back[v]
        front[back[v]] = front[v]
        front[v] = -1
        back[v] = -1
from collections import defaultdict

N  = int(input())
A = list(map(int, input().split()))
Q = int(input())


for i in range(Q):
    query = list(map(int, input().split()))

    # insert
    if query[0]==0:
        k = query[1]
        v = query[2]

        A= A[:k]+[v]+A[k:]

    # erase
    elif query[0]==1:
        k = query[1]
        A.pop(k)

    # count
    else:
        v = query[1]

        cnt = 0
        for num in A:
            if num == v:
                cnt += 1
        print(cnt)
            
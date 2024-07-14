# TLE

import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = [-1] + list(map(int, input().split()))
Q = int(input())




children = [[] for _ in range(N)]
for i in range(1, N):
    children[A[i]].append(i)


def count_boxes_inside_of(v):

    #　中に箱がなくなったら終わり
    if len(children[v]) == 0:
        return 0

    # 中に箱がまだあるとき。
    else:
        total = 0
        for nv in children[v]:
            total += 1
            total += count_boxes_inside_of(nv)
        return total



for _ in range(Q):
    v = int(input())
    ans = count_boxes_inside_of(v)
    print(ans)
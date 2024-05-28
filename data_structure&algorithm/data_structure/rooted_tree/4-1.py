# 時間かかって修正何度もして正解なので、もう一度


numbers = []

def rec(inner_boxes, v):
    numbers.append(v)

    for nv in inner_boxes[v]:
        rec(inner_boxes, nv)

    return


N = int(input())
A = [-1] + list(map(int, input().split()))

inner_boxes = [[] for _ in range(N)]

for i in range(1, N):
    inner_boxes[A[i]].append(i)


rec(inner_boxes, 0)

print(*numbers)

N = int(input())
A = [-1] + list(map(int, input().split()))

inner_boxes = [[] for _ in range(N)]
for i in range(1,N):
    inner_boxes[A[i]].append(i)

opened_boxes = []


def rec(v):
    opened_boxes.append(v)

    for nv in inner_boxes[v]:
        rec(nv)



rec(0)

print(*opened_boxes)
N = int(input())
A = [-1] + list(map(int, input().split()))

inner_boxes = [[] for _ in range(N)]
for i in range(1,N):
    inner_boxes[A[i]].append(i)

numbers = []

def rec(inner_boxes,v):
    numbers.append(v)
    for nv in inner_boxes[v]:
        rec(inner_boxes, nv)




rec(inner_boxes, 0)

print(*numbers)

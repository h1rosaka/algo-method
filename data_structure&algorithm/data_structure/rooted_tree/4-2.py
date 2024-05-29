N = int(input())
A = [-1] + list(map(int, input().split()))

inner_boxes = [[] for _ in range(N)]

for i in range(1,N):
    inner_boxes[A[i]].append(i)

numbers = []

def rec(inner_boxes,box_id):
    numbers.append(box_id)

    for inside_box_id in inner_boxes[box_id]:
        rec(inner_boxes, inside_box_id)

rec(inner_boxes, 0)

print(*numbers)

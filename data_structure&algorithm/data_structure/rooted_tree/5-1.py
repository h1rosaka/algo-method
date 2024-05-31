N = int(input())
A = [-1] + list(map(int, input().split()))


inner_boxes = [[] for _ in range(N)]
for i in range(1,N):
    inner_boxes[A[i]].append(i)


numbers = []

def rec(v):
    for v2 in inner_boxes[v]:
        rec(v2)
    numbers.append(v)


rec(0)




print(*numbers)
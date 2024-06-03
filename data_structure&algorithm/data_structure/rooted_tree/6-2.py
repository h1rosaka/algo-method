N = int(input())
A = [-1] + list(map(int, input().split()))
v = int(input())


inner_boxes = [[] for _ in range(N)]
for i in range(1,N):
    inner_boxes[A[i]].append(i)



count = 0
def rec(v):
    for nv in inner_boxes[v]:
        global count
        count += 1
        rec(nv)
rec(v)
print(count)
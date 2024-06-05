N = int(input())
A = [-1] + list(map(int, input().split()))
Q = int(input())

inner_boxes = [[] for _ in range(N)]
for i in range(1, N):
    inner_boxes[A[i]].append(i)

count = 0
def rec(v):
    global count
    for nv in inner_boxes[v]:
        count += 1
        rec(nv)
    
    
    return count


count = 0
for _ in range(Q):
    v = int(input())
    print(rec(v))
    count = 0
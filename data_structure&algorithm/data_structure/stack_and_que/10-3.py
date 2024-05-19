from collections import deque


X = int(input())
Q = int(input())

todo_que = deque([])

count = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[1]
    if query[0] == 0:
        todo_que.append(t+X)
    else:
        while len(todo_que)>0 and todo_que[0] <= t: 
            todo_que.popleft()
            count += 1
        print(count)

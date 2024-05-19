import queue


Q = int(input())

todo = queue.Queue()

for _ in range(Q):
    query = list(input().split())

    if query[0] == "0":
        s = query[1]
        todo.put(s)

    else:
        print(todo.get())



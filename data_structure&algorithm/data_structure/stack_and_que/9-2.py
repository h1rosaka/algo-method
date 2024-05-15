# お手製que
Q = int(input())

to_do_list = [-1 for _ in range(Q)]
head = 0
tail = 0


for _ in range(Q):
    query = list(input().split())

    if query[0] == "0":
        new_task = query[1]

        to_do_list[tail] = new_task
        tail += 1
        if tail == Q:
            tail = 0
        
    else:
        print(to_do_list[head])
        to_do_list[head] = -1
        head += 1
        if head == Q:
            head = 0
Q = int(input())

to_do_list = []

for _ in range(Q):
    query = list(input().split())
    
    if query[0]  == "0":
        new_task = query[1]
        to_do_list.append(new_task)

    else:
        print(to_do_list.pop(0))

Q = int(input())

data_structer = set()


for _ in range(Q):
    query_type, T = input().split()

    if query_type == "0":
        data_structer.add(T)
    elif query_type == "1":
        data_structer.remove(T)
    else:
        if T in data_structer:
            print("Yes")
        else:
            print("No")


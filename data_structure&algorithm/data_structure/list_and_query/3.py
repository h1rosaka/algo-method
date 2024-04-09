Q = int(input())
mylist = [3,1,4,1,5,9,2,6,5,3]
for i in range(Q):
    query = list(map(int, input().split()))
    query_kind = query[0]
    k = query[1]
    if query_kind == 0:
        print(mylist[k])
    else:
        v = query[2]
        mylist[k] = v
    
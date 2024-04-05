N = int(input())
A = list(map(int, input().split()))
Q = int(input())


for i in range(Q):
    query = list(map(int, input().split()))

    # print(query)

    if query[0]==0:
        newA = []

        for i in range(len(A)-1, -1, -1):
            newA.append(A[i])

        A = newA 

    elif query[0]==1:
        v = query[1]
        A.append(v)
    
    else:
        if len(A)==0:
            print("Error")
        else:
            print(A.pop())
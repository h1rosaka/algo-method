N = int(input())
A = list(map(int,input().split()))
Q = int(input())

A.reverse()


for i in range(Q):
    query = list(map(int, input().split()))


    if query[0]==0:
        v = query[1]
        A.append(v)

    else:
        if len(A)==0:
            print("Error")
        else:
            print(A.pop())

    

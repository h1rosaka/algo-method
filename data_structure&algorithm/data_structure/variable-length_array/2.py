N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        k = query[1]
        if k > len(A)-1 :
            print("Error") 
        else:
            print(A[k])
    else:
        v = query[1]
        A.append(v)

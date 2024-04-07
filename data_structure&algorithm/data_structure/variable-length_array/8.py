from copy import deepcopy

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

a_front = []

for i in range(Q):
    query = list(map(int, input().split()))


    if query[0]==0:
        v = query[1]
        # 一番後ろに足しておいて、後でreverseしてからAと合体 (reverseも時間かかるからなしで)
        a_front.append(v)

    elif query[0]==1:
        v = query[1]
        A.append(v)

    
    else:
        k = query[1]
        #　欲しいものがa_frontの中にある場合 [ 1,2,3,4]をひっくり返して[4,3,2,1]にしてから0番目
        if k <= len(a_front)-1:
            print(a_front[-(k+1)])

        # Aの中にある場合
        else:
            new_k = k - len(a_front)
            if len(A)-1 < new_k:
                print("Error")
            else:
                print(A[new_k])

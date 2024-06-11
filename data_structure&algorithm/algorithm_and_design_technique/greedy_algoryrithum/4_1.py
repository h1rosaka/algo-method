N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_used = [0 for _ in range(M)]


A.sort()
#　勿体無いのは、ある荷物を、自分より大分大きい箱に入れてしまうこと。どれもギリギリちょうどくらいの箱に入れたい

num_packed = 0
for i in range(N):
    # check from smallest box to biggest box
    for j in range(M):
        if A[i] <= B[j] and B_used[j] != 1 :
            num_packed +=1
            B_used[j] = 1
            break
   
print(num_packed)
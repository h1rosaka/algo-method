N, X = map(int, input().split())
A = list(map(int, input().split()))


def func(i,j):
    if i == 0:
        if j == 0:
            return True
        else:
            return False
    else:
        flag = False
        if j >= A[i-1] and func(i-1, j-A[i-1])==True:
            flag = True  # A[i-1]を選んだ
        if func(i-1, j) == True:
            flag = True # A[i-1]を選ばない
        return flag

if func(N, X) == True:
    print("Yes")
else:
    print("No")
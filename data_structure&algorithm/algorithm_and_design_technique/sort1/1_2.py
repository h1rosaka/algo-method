N = int(input())
A = list(map(int, input().split()))



while True:
    switch_happend = False
    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            switch_happend = True
    if switch_happend:
        print(*A)
    else:
        break

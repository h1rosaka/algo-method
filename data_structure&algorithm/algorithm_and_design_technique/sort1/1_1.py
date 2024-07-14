N = int(input())
A = list(map(int, input().split()))

switch_count = 0

while True:
    switch_count = 0

    # 1
    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            switch_count += 1

    if switch_count == 0:
        break
   
    print(*A)
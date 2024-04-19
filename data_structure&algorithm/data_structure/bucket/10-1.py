# TLE
N = int(input())
A = list(map(int,input().split()))
Q = int(input())

for _ in range(Q):
    x = int(input())
    muptile_cnt = 0

    # O(N)
    for a in A:
        if a % x == 0:
            muptile_cnt += 1

    print(muptile_cnt)

# 全体でO(NQ) 10^10 

# 先に全てのxに対して答えを作っておけば、プラスで5*10^5かかるけど、一回あたりは減らせるかも？
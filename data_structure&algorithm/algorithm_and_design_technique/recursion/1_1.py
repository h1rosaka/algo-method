import sys
sys.setrecursionlimit(10**6)
N = int(input())

def func(x):

    if x == 0:
        return 0
    else:
        return x + func(x-1)

print(func(N))
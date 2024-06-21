import sys
sys.setrecursionlimit(10**5)

def rec(a,b):
    if a > b:
        return 0
    else:
        return a + rec(a+1, b)

A, B = map(int, input().split())
print(rec(A,B))
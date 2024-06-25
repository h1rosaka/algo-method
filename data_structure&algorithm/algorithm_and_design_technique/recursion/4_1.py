N = int(input())
fib = [-1 for _ in range(N+1)]

fib[0] = 0
fib[1] = 1

def func(x):
    if fib[x] != -1:
        return fib[x]
    else:
        fib[x] = func(x-1) + func(x-2)
        return fib[x]
print(func(N))
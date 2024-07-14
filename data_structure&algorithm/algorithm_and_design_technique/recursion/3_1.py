def func(x):

    if x == 0:
        return 0

    elif x == 1:
        return 1

    else:
        return func(x-2) + func(x-1)


N = int(input())

print(func(N))
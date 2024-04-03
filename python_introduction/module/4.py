import itertools

# ここにコードを書いてください
for i, j, k in itertools.product(range(1,22), repeat=3):
    if i**2 + j**2 == k**2:
        print(i, j, k)
# まだTLEな箇所がある
# 先に、Pごとに、満たす整数x,yのくみが何個あるか数えておく


num_couples_to_make_p = [0 for _ in range(10001)]


for x in range(-100,101):
    for y in range(-100,101):
        p = x**2 + y**2
        if p <= 10000:
            num_couples_to_make_p[p] += 1

Q = int(input())

for _ in range(Q):
    P = int(input())
    print(num_couples_to_make_p[P])







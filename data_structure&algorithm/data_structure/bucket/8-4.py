

Q = int(input())

p_list = []
for _ in range(Q):
    p_list.append(int(input()))

num_couples_to_make_p = [0 for _ in range(20001)]

for x in range(-100,101,1):
    for y in range(-100,101,1):
        p = x**2 + y**2
        num_couples_to_make_p[p] += 1


for i in range(Q):
    p = p_list[i]
    print(num_couples_to_make_p[p])

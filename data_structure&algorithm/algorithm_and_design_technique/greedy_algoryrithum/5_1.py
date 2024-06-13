N = int(input())

num_cakes_left = N
days = 0

# eat backward
while num_cakes_left !=0:

    if num_cakes_left % 3 == 0:
        num_cakes_left //= 3
        days += 1

    else:
        num_cakes_left -= 1
        days += 1

print(days)
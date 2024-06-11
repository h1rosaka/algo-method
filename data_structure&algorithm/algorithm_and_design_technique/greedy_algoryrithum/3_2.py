X = int(input())
A = list(map(int, input().split()))


coins = [50, 10, 5, 1]

rest = X
num_necessary_coins = 0
for i in range(4):
    coin_price = coins[i]
    num_potential_addition = rest // coin_price
    num_addition = min(A[i], num_potential_addition)
    num_necessary_coins += num_addition
    rest -= coin_price*num_addition
print(num_necessary_coins)

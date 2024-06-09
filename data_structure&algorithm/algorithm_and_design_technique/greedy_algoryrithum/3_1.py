X = int(input())
A = list(map(int, input().split()))

coin_price_list = [50, 10, 5, 1]

num_neccesary_coins = 0
rest = X

for i in range(4):
    coin_price = coin_price_list[i]

    for _ in range(1,A[i]+1):
        if rest >= coin_price:
            rest -= coin_price
            num_neccesary_coins += 1
print(num_neccesary_coins)
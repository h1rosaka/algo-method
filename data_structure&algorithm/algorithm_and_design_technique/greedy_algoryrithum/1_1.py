N = int(input())

rest = N
five_yen_coin_count = 0

while rest >= 5:
    rest -= 5
    five_yen_coin_count += 1

print(five_yen_coin_count + rest)
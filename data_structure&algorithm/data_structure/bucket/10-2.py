N = int(input())
A = list(map(int,input().split()))
Q = int(input())


a_max = 5*(10**5) #TODOかっこいらない？

# Aをその値ごとに何個あるか把握するバケット
a_counter = [0 for _ in range(a_max+1)]
for a in A:
    a_counter[a] += 1

# 同じ問題が来た時に、数えなくても答えられるようにする
known_answers = [-1 for _ in range(a_max+1)]

for _ in range(Q):
    x = int(input())

    if known_answers[x] != -1:
        print(known_answers[x])

    else:
        checking_target = x
        num_multiples = 0

        while checking_target <= a_max:
            num_multiples += a_counter[checking_target]
            checking_target += x
        
        known_answers[x] = num_multiples

        print(known_answers[x])
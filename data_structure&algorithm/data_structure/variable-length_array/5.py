N = int(input())


numbers = [i+1 for i in range(N)]
target_id = 0

while len(numbers)>=2: 


    #残っているもののうち、２番目に近い値を次のターゲットにする
    # i番目をpopしたのなら、元の配列で言うi+2番目、つまりはpop後のi+1番目がターゲット

    numbers.pop(target_id)
    target_id += 1

    # レンジから外れたら先頭から数え直す
    if target_id >= len(numbers):
        target_id -= len(numbers)
    
    # target_id = 5で11をpopした後、target_id = 6になるが配列の長さは6しかなくて最大indexは5
    # 次消すべきは2でその順番は0

print(numbers[0])

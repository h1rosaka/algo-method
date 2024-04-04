import copy

# ここに答えとなるコードを書いてください
ppl = ["A", "B", "C", "D"]
order = []


"""
一人目を選ぶ&残り3人のセットを作る
二人目を選ぶ&残り2人のセットを作る
三人目を選ぶ
残りを足す
"""


# order.append(person)

for person in ppl :
    order = [] # 席順リセット
    order.append(person) # Aが入る
    remaining_three = copy.deepcopy(ppl)
    remaining_three.remove(person)
    
    for person in remaining_three:
        order.append(person) # Bが入る
        remaining_two = copy.deepcopy(remaining_three)
        remaining_two.remove(person)


        # print(*(order+remaining_two))
        # print(*(order+remaining_two[::-1]))

        print(order[0]+order[1]+remaining_two[0]+remaining_two[1])
        print(order[0]+order[1]+remaining_two[1]+remaining_two[0])

        order.remove(person) # 次のループのためにこの階層で足したものを除く


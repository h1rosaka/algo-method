class Node:
    def __init__(self, value=""):
        self.nex = None
        self.value = value

# 連結リストの初期化
nil = Node()
nil.nex = nil
# nilは値がNoneで次がnil(自分自身？)

# 連結リストの先頭への要素の挿入
def insert(v):
    v.nex = nil.nex # 挿入するノードvの矢印の先を、nilが指してる矢印の先のやつにあるやつに設定
    nil.nex = v  # nil(いつも先頭にあるやつ)の次のやつを、挿入するノードvにする


Q = int(input())
for _ in range(Q):
    query_type, S = input().split()

    if query_type == "0":
        v = Node(S)
        insert(v)

    else:
        # 先頭から k (=S) 個
        v = nil
        for i in range(int(S)):
            v = v.nex;
            if v == nil:
                break
            print(v.value, end = ' ')
        print()




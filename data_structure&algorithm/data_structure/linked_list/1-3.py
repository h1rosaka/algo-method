class Node():
    def __init__(self, value=None):
        self.nex = None
        self.value = value # 同じ名前使う？

nil = Node()
nil.nex = nil

def insert(new_node):
    new_node.nex = nil.nex
    nil.nex = new_node

num_queries = int(input())
for i in range(num_queries):
    query = input().split()

    if query[0] == "0":
        given_string_s = query[1] # 場合分け方法これで良い？
        new_node = Node(given_string_s)
        insert(new_node)
    elif query[0] == "1": # ただのelseと書くのどっちがいいんだろうか
        given_int_k = int(query[1])
        target_node = nil.nex
        for i in range(given_int_k):
            if target_node == nil:
                break
            print(target_node.value, end =" ")
            target_node = target_node.nex
        print()


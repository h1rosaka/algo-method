class Node():
    def __init__(self, value):
        self.nex = None
        self.value = value

nil = Node(None)
nil.nex = nil


def create_node_and_insert(string):
    new_node = Node(string)

    new_node.nex = nil.nex
    nil.nex = new_node
    

Q = int(input())

for _ in range(Q):
    query = input().split()

    if query[0] == "0":
        S = query[1]
        create_node_and_insert(S)
    else:
        k = int(query[1])
        current_node = nil.nex
        cnt = 0
        while current_node != nil:
            if cnt >= k:
                break
            else:
                print(current_node.value, end = " ")
                current_node = current_node.nex
                cnt += 1

        print()



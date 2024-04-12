class Node():
    def __init__(self, v=''):
        self.nex = None
        self.pre = None
        self.value = v

nil = Node()
nil.nex = nil
nil.pre = nil



def push_head(s):
    new_node = Node(s)
    
    new_node.nex = nil.nex
    nil.nex.pre = new_node

    nil.nex = new_node
    new_node.pre = nil


def pop_tail():
    target_node = nil.pre

    if target_node == nil:
        print('Error')
    else:
        print(target_node.value)
        target_node.pre.nex = nil
        nil.pre = nil.pre.pre
        del target_node


Q = int(input())
for _ in range(Q):
    query = input().split()

    if query[0] == '0':
        push_head(query[1])
    else:
        pop_tail()
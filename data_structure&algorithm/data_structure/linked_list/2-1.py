class Node():
    def __init__(self, v=""):
        self.value = v
        self.nex = None

nil = Node()
nil.nex = nil

num_queries = int(input())

def push_heads(s):
    new_node = Node(s)
    new_node.nex = nil.nex
    nil.nex = new_node 

def pop_heads():
    if nil.nex == nil:
        print('Error')
    else:
        print(nil.nex.value)
        nil.nex = nil.nex.nex

for _ in range(num_queries):
    query = input().split()

    if query[0]=='0':
        S = query[1]
        push_heads(S)
    else:
        pop_heads()






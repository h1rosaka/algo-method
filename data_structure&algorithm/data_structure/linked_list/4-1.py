# 一部　WAだがあってそうに見える
class Node:
    def __init__(self, value=""):
        self.nex = None
        self.prev = None
        self.value = value

nil = Node()
nil.nex = nil
nil.prev = nil

def push_head(s):
    new_node = Node(s)
    new_node.nex = nil.nex
    nil.nex = new_node
    nil.nex.prev = new_node
    new_node.prev = nil

def push_tail(s):
    new_node = Node(s)
    new_node.nex = nil
    nil.prev.nex = new_node
    new_node.prev = nil.prev
    nil.prev = new_node

def pop_head():
    if nil.nex == nil:
        print("Error")
    else:
        print(nil.nex.value)
        nil.nex.nex.prev = nil
        nil.nex = nil.nex.nex

def pop_tail():
    if nil.nex == nil:
        print("Error")
    else:
        print(nil.prev.value)
        nil.prev.prev.nex = nil
        nil.prev = nil.prev.prev

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    query_type = query[0]
    if query_type == "0":
        s = query[1]
        push_head(s)
    elif query_type == "1":
        s = query[1]
        push_tail(s)
    elif query_type == "2":
        pop_head()
    elif query_type == "3":
        pop_tail()
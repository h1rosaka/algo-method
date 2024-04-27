#連結リストのpushは、まずは新しく追加するノードから矢印伸ばして、その後、既存の矢印を新ノードに。

# 一部　WAだがあってそうに見える
class Node:
    def __init__(self, value=""):
        self.nex = None
        self.pre = None
        self.value = value

nil = Node()
nil.nex = nil
nil.pre = nil

def push_head(v):
    #　まず新しく追加するノードから矢印を伸ばす
    v.nex = nil.nex
    v.pre = nil
    # 次に既存のノードからの矢印を修正
    nil.nex = v
    v.nex.pre = v


def push_tail(v):
    #まず、新しく追加するノードから矢印を伸ばす
    v.nex = nil
    v.pre = nil.pre
    # 次に既存の矢印を修正してvに向ける
    nil.pre = v
    v.pre.nex = v

def pop_head():
    head = nil.nex
    if  head == nil:
        print("Error")
    else:
        print(head.value)
        head.nex.pre = nil
        nil.nex = head.nex

def pop_tail():
    tail = nil.pre
    if nil.pre == nil:
        print("Error")
    else:
        print(tail.value)
        tail.pre.nex = nil
        nil.pre = tail.pre

Q = int(input())
for _ in range(Q):
    query = list(input().split())
    query_type = query[0]

    if query_type == "0":
        s = query[1]
        v = Node(s)
        push_head(v)

    elif query_type == "1":
        s = query[1]
        v = Node(s)
        push_tail(v)

    elif query_type == "2":
        pop_head()

    elif query_type == "3":
        pop_tail()
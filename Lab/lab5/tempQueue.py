class tempQueue:
    class tnode():
        def __init__(self, k, v):
            self.key = k
            self.name = v
    def __init__(self):
        self.list = []
        
    def isEmpty(self):
        return len(self.list) == 0
    def Minimum(self):
        min_node = min(list(self.list), key=lambda x:x.key, default=None)
        return min_node

    def Insert(self, k, v):
        new = self.tnode(k, v)
        self.list.append(new)
        return new
    def ExtractMin(self):
        min_node = min(list(self.list), key=lambda x:x.key, default=None)
        self.list.remove(min_node)
        return min_node.name
    def DecreaseKey(self, n, k2):
        n.key = k2
def MakeHeap():
    return tempQueue()

import fib
import tempQueue
class Vertex:
    name = ''
    def __init__(self, n):
        self.name = n

class Edge:
    def __init__(self, w = 0, s = None, e = None):
        self.weight = w
        self.start = s
        self.end = e

class DenseGraph:

    def __init__(self):
        self.VertexCount = 0
        self.NameDict = {}
        self.EdgeCount = 0
        self.EdgeTable = []
        self.VertexList = []

    def AddEdge(self, u, v, weight):
        if self.NameDict.get(u) == None:
            self.AddVertex(u)
        if self.NameDict.get(v) == None:
            self.AddVertex(v)
        self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] = weight
        self.EdgeCount += 1

    def AddVertex(self, u):
        self.NameDict[u] = self.VertexCount
        self.VertexCount += 1
        self.EdgeTable.append([None for i in range(self.VertexCount)])
        for i in range(self.VertexCount - 1):
            self.EdgeTable[i].append(None)
        self.VertexList.append(u)

    def GetVertexValue(self, u):
        #print(u)
        return self.NameDict[u]

#################################################  

    def RemoveEdge(self, u, v):
        self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] = None
        self.EdgeCount += -1

    def RemoveVertex(self, u):
        del self.NameDict[u]
        index = self.GetVertexValue(u)
        for i in range(self.VertexCount):
            self.EdgeTable[i].pop(index)
        self.EdgeTable.pop(index)
        self.VertexCount += -1

    def IsAdjacent(self, u, v):
        if self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] or EdgeTable[self.GetVertexValue(v)][self.GetVertexValue(u)]:
            return True
        return False

    def GetEdgeWeight(self, u, v):
        return self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)]

    def SetEdgeWeight(self, u, v, weight):
        if self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)]:
            self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] = weight

    def SetVertexValue(self, u, value):
        self.NameDict[u] = value

def Dijkstra():
    LineCount = int(input())
    G = DenseGraph()
    for i in range(LineCount):
        Line = input().split()
        u = Line[0]
        v = Line[1]
        weight = int(Line[2]) 
        G.AddEdge(u, v, weight)
    s = input()
    t = input()
    #print(G.NameDict)

    PrevList = [None] * G.VertexCount
    DistList = [1_000_000] * G.VertexCount
    DistList[G.GetVertexValue(s)] = 0

    S = fib.MakeHeap()
    for i in range(G.VertexCount):
        S.Insert(DistList[i], G.VertexList[i])

    probe = S.min_node
    children = {}
    children[probe.name] = probe
    probe = probe.right
    while (probe != S.min_node):
        children[probe.name] = probe
        probe = probe.right

    # l = S.list
    # children = {}
    # for n in l:
    #     children[n.name] = n

    v = s
    while v != t:
        for u, w in enumerate(G.EdgeTable[G.GetVertexValue(v)]):
            if w != None:
                tmp = DistList[G.GetVertexValue(v)] + w
                if tmp < DistList[u]:
                    DistList[u] = tmp
                    S.DecreaseKey(children[G.VertexList[u]], tmp)
                    PrevList[u] = v
        S.ExtractMin()
        v = S.Minimum().name

    result = []
    while t != s:
        result.append(t)
        t = PrevList[G.GetVertexValue(t)]
    result.append(s)
    result.reverse()
    return result

print(Dijkstra())





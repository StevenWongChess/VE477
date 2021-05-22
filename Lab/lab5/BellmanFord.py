class Vertex:
    name = ''
    def __init__(self, n):
        self.name = n

class Edge:
    def __init__(self, s = None, e = None, w = 0):
        self.weight = w
        self.start = s
        self.end = e
    def __repr__(self):
        return str(self.start) + str(self.end)

class DenseGraph:

    def __init__(self):
        self.VertexCount = 0
        self.NameDict = {}
        self.EdgeCount = 0
        self.EdgeList = []
        self.EdgeTable = []
        self.VertexList = []

    def AddEdge(self, u, v, weight):
        if self.NameDict.get(u) == None:
            self.AddVertex(u)
        if self.NameDict.get(v) == None:
            self.AddVertex(v)
        self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] = weight
        self.EdgeCount += 1
        self.EdgeList.append(Edge(u, v, weight))

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

def BellmanFord():
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
    
    dist = [1_000_000] * G.VertexCount
    prev = [None] * G.VertexCount

    dist[G.GetVertexValue(s)] = 0

    for j in range(G.VertexCount):
        for i in G.EdgeList: 
            tmp = dist[G.GetVertexValue(i.start)] + i.weight
            if tmp < dist[G.GetVertexValue(i.end)]:
                dist[G.GetVertexValue(i.end)] = tmp
                prev[G.GetVertexValue(i.end)] = i.start

    result = []
    while t != s:
        #print('once', t)
        result.append(t)
        t = prev[G.GetVertexValue(t)]
    result.append(s)
    result.reverse()
    return result

print(BellmanFord())





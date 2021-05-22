import queue

class Vertex:
    name = ''
    def __init__(self, n):
        self.name = n

class Edge:
    def __init__(self, s = None, e = None, w = 0):
        self.start = s
        self.end = e
        self.weight = w
    def __repr__(self):
        return str(self.start) + str(self.end)

class DenseGraph:

    def __init__(self):
        self.VertexCount = 0
        self.VertexList = []

        self.NameDict = {}

        self.EdgeCount = 0
        #self.EdgeList = []
        self.EdgeTable = []

    def AddEdge(self, u, v, weight):
        if self.NameDict.get(u) == None:
            self.AddVertex(u)
        if self.NameDict.get(v) == None:
            self.AddVertex(v)
        self.EdgeTable[self.GetVertexValue(u)][self.GetVertexValue(v)] = weight
        self.EdgeCount += 1
        #self.EdgeList.append(Edge(u, v, weight))

    def AddVertex(self, u):
        self.NameDict[u] = self.VertexCount
        self.VertexCount += 1
        self.EdgeTable.append([0 for i in range(self.VertexCount)])
        for i in range(self.VertexCount - 1):
            self.EdgeTable[i].append(0)
        self.VertexList.append(u)

    def GetVertexValue(self, u):
        #print(u)
        return self.NameDict[u]

def BFS(G, s, t):
	#q = queue.Queue()
	visited = [False] * G.VertexCount
	parent = [None] * G.VertexCount
	s = G.GetVertexValue(s)
	visited[s] = True
	q = [s]
	
	t = G.GetVertexValue(t)
	#path = {s:[]}

	while(q):
		u = q.pop(0)
		for v in range(G.VertexCount):
			if G.EdgeTable[u][v] > 0 and not visited[v]:
				visited[v] = True
				#path[v] = path[u] + [(u,v)]
				parent[v] = u
				if v == t:
					path = []
					while(v != s):
						path.append([parent[v], v])
						v = parent[v]
					path.reverse()
					return path
				q.append(v)
		#print(q)
	return None

def EdmondsKarp():
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

    # F = [[0] * LineCount for i in range(LineCount)]
    path = BFS(G, s, t)
    #print(path)
    sum=0
    while path != None:
    	flow = min(G.EdgeTable[u][v] for u, v in path)
    	# flow = float('Inf')
    	# for u,v in path:
    	# 	flow = min(G.EdgeTable[u][v], flow)
    	sum += flow
    	for u, v in path:
    		G.EdgeTable[u][v] -= flow
    		G.EdgeTable[v][u] += flow
    	path = BFS(G, s, t)

    return sum

print(EdmondsKarp())


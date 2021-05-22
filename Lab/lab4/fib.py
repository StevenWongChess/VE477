import math

class FibonacciHeap:
	"""docstring for ClassName"""
	class Node:
		def __init__(self, key):
			self.key = key
			self.parent = None
			self.child = None
			self.left = None
			self.right = None
			self.degree = 0
			self.mark = False

	min_node = None
	n = 0

	def __init__(self): # MakeHeap
		min_node = None
		n = 0

	def together(self, x, y):
		y.right.left = y.left
		y.left.right = y.right
		y.parent = x
		x.degree += 1
		if x.degree > 1:
			y.left = x.child
			y.right = x.child.right
			x.child.right.left = y
			x.child.right = y
		else:
			x.child = y
			y.left = y
			y.right = y

	def consolidate(self):
		A = [None] * int(math.log(self.n) * 2)
		probe = self.min_node
		children = [probe]
		probe = probe.right
		while (probe != self.min_node):
			children.append(probe)
			probe = probe.right
		for x in children:
			d = x.degree
			while A[d] != None:
				y = A[d]
				if x.key < y.key:
					self.together(x, y)
				else:
					self.together(y, x)
				A[d] = None
				d += 1
			A[d] = x
		for i in A:
			if i is not None and i.key < self.min_node.key:
				self.min_node = i

	def Minimum(self):
		return self.min_node;

	def Insert(self, value):
		node = self.Node(value)		
		if (self.min_node is None):
			node.left = node
			node.right = node
			self.min_node = node
		else:
			node.left = self.min_node
			node.right = self.min_node.right
			self.min_node.right.left = node
			self.min_node.right = node
			if (self.min_node.key > node.key):
				self.min_node = node
		self.n += 1

	def Insert_node(self, node):
		if self.min_node is None:
			min_node = node
			node.left = node
			node.right = node
		else:
			node.left = self.min_node
			node.right = self.min_node.right
			self.min_node.right.left = node
			self.min_node.right = node

	def ExtractMin(self):
		temp = self.min_node
		if temp.child is not None:
			probe = temp.child
			children = [probe]
			probe = probe.right
			while (probe != temp.child):
				children.append(probe)
				probe = probe.right
			temp.child = None
			for i in children:
				i.parent = None
				self.Insert_node(i)
		temp.right.left = temp.left
		temp.left.right = temp.right
		self.min_node = temp.right
		self.consolidate()
		#self.updatemin()

	def DecreaseKey(self, node, value):
		node.key = value
		father = node.parent
		if (node.key < self.min_node.key):
			self.min_node = node
		if (father is not None and node.key < father.key):
			self.Insert_node(node)
			father.degree -= 1
			if father.degree == 0:
				father.child = None
			else:
				father.child = node.right
				node.right.left = node.left
				node.left.right = node.right
			if (father.mark == False):
				father.mark = True
			else:
				father.mark = False
				self.DecreaseKey(father, father.key)		

	def Delete(self, node):
		self.DecreaseKey(node, -1) # assume others are \in N^+
		self.ExtractMin()

	def printlist(self, node):
		if node is None:
			return
		probe = node
		print("layer----")
		print(probe.key)
		self.printlist(probe.child)
		probe = probe.right
		while (probe != node):
			print(probe.key)
			self.printlist(probe.child)
			probe = probe.right

def MakeHeap():
	return FibonacciHeap()

def Union(h1, h2):
	h = MakeHeap()
	h.min_node = h1.min_node if h1.min_node.key < h2.min_node.key else h2.min_node
	h.n = h1.n + h2.n

	temp = h1.min_node.right
	h1.min_node.right.left = h2.min_node.left
	h1.min_node.right = h2.min_node
	h2.min_node.left.right = temp
	h2.min_node.left = h1.min_node
	return h

def test():
    A = MakeHeap()
    for i in range(10):
    	A.Insert(3*i+1)
    B = MakeHeap()
    for i in range(10):
    	B.Insert(3*i+3)
    A.ExtractMin()
    B.ExtractMin()
    C = Union(A, B)
    C.ExtractMin()
    C.printlist(C.min_node)
    C.DecreaseKey(C.min_node.right, 1)
    C.printlist(C.min_node)

if __name__=='__main__':
    test()

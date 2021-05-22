import random
import time

def RandomSearch(A, k):
	n = len(A)
	visited = {i: 1 for i in range(n)}
	while len(visited):
		i = random.randint(0,n-1)
		if not visited.get(i):
			continue
		visited.pop(i)
		if A[i] == k:
			return "Found"
	return "Not Found"

def LinearSearch(A, k):
	n = len(A)
	for i in range(n):
		if A[i] == k:
			return "Found"
	return "Not Found"

def ScrambleSearch(A, k):
	random.shuffle(A)
	LinearSearch(A, k)

# test function
size = 1_000_000
times = 1_00#0

timer1 = 0
timer2 = 0
timer3 = 0

for i in range(times):
	# a = time.time()
	A = [random.randint(1, size) for j in range(size)]
	# b = time.time()
	# print("here", b-a)
	k = random.randint(1, size)

	start1 = time.time()
	RandomSearch(A, k)
	end1 = time.time()
	timer1 += end1 - start1

	start2 = time.time()
	LinearSearch(A, k)
	end2 = time.time()
	timer2 += end2 - start2

	start3 = time.time()
	ScrambleSearch(A, k)
	end3 = time.time()
	timer3 += end3 - start3

	print("round =", i)

print("RandomSearch", timer1/times)
print("LinearSearch", timer2/times)
print("ScrambleSearch", timer3/times)





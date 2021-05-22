prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
test = [1 for i in range(0, 100)]
for p in prime:
	for q in prime:
		if p + q < 100:
			test[p+q] = 0

m_pool = []
for i in range(5, 100):
	if test[i] == 1:
		m_pool.append(i)
print(m_pool)
n_pool = []
for m in m_pool:
	for i in range(2, m - 1):
		if not i in prime and (m - i) in prime:
			print(m, "=", i, "+", (m-i), "multiple", (i*(m-i)))
			if i*(m-i) > 3000:
				print("hahah")
			n_pool.append(i*(m-i))
print("the n_pool is", n_pool)
smaller = []
times = [0] * 3000
for i in n_pool:
	times[i] += 1
for i in range(3000):
	if times[i] == 1:
		smaller.append(i)
print(smaller)

ind = [0] * 100
for m in m_pool:
	for i in range(2, m - 1):
		if not i in prime and (m - i) in prime:
			if i*(m-i) in smaller:
				ind[m] += 1
answer = []
for i in range(100):
	if ind[i] == 1:
		answer.append(i)
print(answer)



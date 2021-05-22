
#data = [[2,4], [9,13], [6,12]]

def Cmp(a, b):
	if a[0] > b[0]: return True
	if a[0] < b[0]: return False
	if a[1] > b[1]: return True
	if a[1] < b[1]: return False
	return False

# for p in range(len(data)):
# 	for q in range(len(data)-p-1):
# 		if Cmp(data[q], data[q+1]):
# 			tmp = data[q]
# 			data[q] = data[q+1]
# 			data[q+1] = tmp

P, hc = input().split()
P = int(P)
hc = int(hc)

S = []
T = []
H = []
for i in range(P):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    S.append(a)
    T.append(b)
    H.append(c)

n = int(input())
C = []  
for i in range(n):
    a = int(input())
    C.append(a)

results = [-1] * n
for i in range(P):
	for j in range(i+1):
		choose = [True] * P
		choose[i] = False
		choose[j] = False
		if i == j and H[i] > hc:
			continue
		if i != j and H[i] + H[j] > hc:
			continue
		data = []
		for k in range(P):
			if choose[k]:
				data.append([S[k], T[k]])
		ddl = 0
		for (a,b) in data:
			if b > ddl:
				ddl = b
		#print(data, "before")
		for p in range(len(data)):
			for q in range(len(data)-p-1):
				if (Cmp(data[q], data[q+1])):
					tmp = data[q]
					data[q] = data[q+1]
					data[q+1] = tmp
		#print(data, "after")					
		result = []
		for a, b in data:
			if not result:
				result.append([a, b])
				continue

			la, lb = result[-1]
			if la <= a <= lb and b > lb:
				result[-1][1] = b
			if a > lb:
				result.append([a, b])
		# cover = ddl
		# for a, b in result:
		# 	cover += (a-b)

		#print(choose)
		#print(result)
# ddl 和 cover
		# for k in range(n):
		# 	if C[k] <= cover:
		# 		if results[k] == -1 or C[k] > ddl:
		# 			results[k] = ddl
		# 	else:
		# 		tmp = C[k] - cover + ddl
		# 		if results[k] == -1 or results[k] > tmp:
		# 			results[k] = tmp
		for k in range(n):
			count = C[k]
			answer = 0
			for z in range(len(result)):
				a, b = result[z]
				if z == 0:
					prev = 0
				else:
					_, prev = result[z-1]
				if count <= a - prev:
					answer = prev + count
					count = 0
					break
				else:
					count += prev - a
			if count > 0:
				answer = ddl + count

			if results[k] == -1 or results[k] > answer:
				results[k] = answer

			#print(results[k],"--", k)
		#print(result, "haha", cover, ddl)

for i in range(n):
	print(results[i])







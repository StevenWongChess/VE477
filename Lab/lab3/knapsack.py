def boring(M, S, result):
	n = len(S)
	table = [[False for i in range(M + 1)] for j in range(n + 1)]

	for i in range(n+1):
		table[i][0] = True
	for j in range(1, M+1):
		table[0][j] = False

	for i in range(1, n+1):
		for j in range(1, M+1):
			if j < S[i-1]:
				table[i][j] = table[i-1][j]
			else:
				table[i][j] = table[i-1][j] or table[i-1][j-S[i-1]]

	ifboring = table[n][M]
	i = n
	summ = M
	if ifboring:
		while i >= 0:
			if table[i][summ] and not table[i-1][summ]:
				result.append(S[i-1])
				#print(result)
				summ = summ - S[i-1]
				if summ == 0:
					return (ifboring, result)
			i = i - 1
	return (ifboring, result)


if __name__ == '__main__':
	total = int(input())
	numbers = [int(n) for n in input().split()]

	if total == 0:
		print([])
	else:
		(answer, resultt) = boring(total, numbers, [])
		if answer:
			resultt.sort()
			print(resultt)
		else:
			pass





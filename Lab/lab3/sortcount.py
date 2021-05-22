def MergeCount(L1, L2):
	count = 0
	L = []
	i = 0
	j = 0
	while (i < len(L1) and j < len(L2)):
		if L1[i] <= L2[j]:
			L.append(L1[i])
			i = i + 1
		else:
			L.append(L2[j])
			count = count + len(L1) - i
			j = j + 1
	if i >= len(L1):
		for t in range(j, len(L2)):
			L.append(L2[t])
	else:
		for t in range(i, len(L1)):
			L.append(L1[t])
	return (count, L)

def SortCount(LL):
	if (len(LL) <= 1):
		return (0, LL)
	else:
		L1 = LL[0: (len(LL)//2)]
		L2 = LL[(len(LL)//2):]
		(count1, L1) = SortCount(L1)
		(count2, L2) = SortCount(L2)
		(count, L) = MergeCount(L1, L2)
	count = count + count1 + count2
	return (count, L)

if __name__ == '__main__':
    numbers = [int(n) for n in input().split()]
    result = SortCount(numbers)
    print(result[0])
    print(result[1])


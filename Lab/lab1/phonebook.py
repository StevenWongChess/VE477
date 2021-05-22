
def main():
	dict = {}
	while True:
		buffer = input().split()
		if (buffer[0] == 'add'):
			dict[buffer[1]] = int(buffer[2])
		elif (buffer[0] == 'edit'):
			if buffer[1] in dict:
				dict[buffer[1]] = int(buffer[2])
		elif (buffer[0] == 'remove'):
			if buffer[1] in dict:
				del dict[buffer[1]]	
		elif (buffer[0] == 'quit'):
			break
		else:
			break
		print(dict)

if __name__ == '__main__':
    main()
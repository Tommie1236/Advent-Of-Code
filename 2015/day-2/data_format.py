data = []
i = 0 #package number

with open('data.txt', 'r') as d:
		for value in d:
			data.append([])
			for size in value.split('x'):
				data[i].append(int(size))
			i += 1


if __name__ == '__main__':
	print(data)
data = ''

with open('data.txt', 'r') as d:
	data = d.read()

if __name__ == '__main__':
	print(data)
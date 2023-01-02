from data_format import data

floor = 0

for i in data:
	if i == '(':
		floor += 1
	elif i == ')':
		floor -= 1

if __name__ == '__main__':
	print(floor)

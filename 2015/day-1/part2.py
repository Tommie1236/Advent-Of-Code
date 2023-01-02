from data_format import data 

floor = 0
j = 0

for i in data:
	j += 1
	if i == '(':
		floor += 1
	elif i == ')':
		floor -= 1
	if floor == -1:
		print(floor)
		print(j)

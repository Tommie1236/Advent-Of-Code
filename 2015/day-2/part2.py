from data_format import data as boxes

ribbon = 0

#boxes = [[2,3,4],[1,1,10]]

for box in boxes:
	l, w, h = size = box
	# removing the biggest size from the list of sizes
	#so only the 2 smallest are left 
	size.remove(max(size))
	wrap = 2*(size[0]+size[1])
	bow = l*w*h
	ribbon += wrap + bow

print(ribbon)
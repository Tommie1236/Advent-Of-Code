from data_format import data as boxes
import pprint
p = pprint.PrettyPrinter()

#boxes = [[2, 3, 4], [1, 1, 10]] # This is test data to check if the script work 
total = 0

# function to calculate the amount of paper needed for a box
def calculate_paper(sizes):
	l, w, h = sizes
	paper = 2*l*w + 2*w*h + 2*h*l
	slack = min(l*w, w*h, h*l)
	return paper + slack


for box in boxes:
	total += calculate_paper(box)




if __name__ == '__main__':
	print(total)
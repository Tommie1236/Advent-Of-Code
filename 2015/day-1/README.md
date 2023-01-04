# Day 1 of 2015

1. I started by copying my input data to a text file ([data.txt](data.txt)).
2. After that I created a python script to put the data in a variable so i can use it. ([data_format.py](data_format.py))
	- Create a variable to store the data `data = ''`
	- Then open a file and store the data in a variable:
		```py
		with open('data.txt', 'r' as d:
		data = d.read()
		```
3. Then I created the main script for part 1 of the puzzle ([part1.py](part1.py))
	- Import the data from the `data_format.py` script:
		```py
		from data_format import data
		```
	- Set the floor to `0`:
		```py
		floor = 0
		```
	- Loop over instructions `i` in the data:
		```py
		for i in data:
		```
	- For each instruction check if the instruction equals `(` or `)` then add or remove a floor respectively:
		```py
		if i == '(':
			floor += 1
		elif i == ')':
			floor -= 1
		```
	- At the end i printed the floor and inserted the answer in the [AoC website](https://adventofcode.com/)
		```py
		print(floor)
		```
<br>

4. For part 2 I copied the script for part 1 and changed some thins:
	- Under the floor variable i created a new variable to keep track of the number of the instructions: `j`.
		```py
		j = 0
		```
	- And incremented it for every instuction
		```py
		for i in data:
			j += 1
		```
	- After the code to change the floor I added a `if` statement to check if the floor is equal to `-1`
		```py
		j += 1
		if i == '(':
			floor += 1
		elif i == ')':
			floor -= 1
		if floor == -1:
		```
	- Inside the if statement I added `print()` statements to display the `floor` and instruction number `j`.  
		I also printed the floor to check if it is `-1`
		```py
		print(floor)
		print(j)
		```
	- Then I read the first value in the output and put it in the answer box.

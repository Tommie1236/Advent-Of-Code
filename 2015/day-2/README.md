# Day 2 of 2015

1. I started by copying my input data to a text file ([data.txt](data.txt)).
2. After that I created a python script to take the box sizes from the [data file](data.txt) and put them into a list so it is easier to work with. ([data_format.py](data_format.py))
    - Create a variable to store the data and another to keep track of the box number:
        ```py
        data = []
        i = 0
        ```
    - Then open the [data file](data.txt) and loop over each box's sizes:
        ```py
        with open('data.txt', 'r') as d:
            for value in d:
        ```
    - Next, append a new list to the data list and split the sizes by the `x` so we get 3 separate values. Then convert the sizes from `str` to `int` and add them to the box sizes:
        ```py
        data.append([])
        for size in value.split('x'):
            data[i].append(int(size))
        ```
    - And last increment the variable that keeps track of the box number:
        ```py
        i += 1 
        ```

3. Then I created the main python script for part 1. ([part1.py](part1.py))
    - Import the data from the [data_format.py](data_format.py) file as boxes (basicly renaming `data` to `boxes`):
        ```py
        from data_format import data as boxes
        ```
    - I also imported and initialised the `pprint()` method from `PrettyPrinter` so the data in the output is easier to read:
        ```py
        from pprint import PrettyPrinter
        p = PrettyPrinter()
        ```
    - Set the total amount of paper needed to `0`:
        ```py
        total = 0
        ```
    - Create a function to calculate the amount of wrapping paper the elves need for each box (present):
        ```py
        def calculate_paper(sizes):
            l, w, h = sizes
            paper = 2*l*w + 2*w*h + 2*h*l
            slack = min(l*w, w*h, h*l)
            return paper + slack
        ```
    - Loop over the list with boxes:
        ```py
        for box in boxes:
        ```
    - Call the `calculate_paper()` function and add the result to the `total` amount of paper:
        ```py
        total += calculate_paper(box) 
        ```
    - Print the answer and put in the answer box:
        ```py
        print(total)
        ```
<br>

4. For part 2 I created a new script: ([part2.py](part2.py))
    - I started by importing the data as `boxes`:
        ```py
        from data_format import data as boxes
        ```
    - Set the amount of `ribbon` needed to `0`:
        ```py
        ribbon = 0
        ```
    - Then loop over the `boxes`:
        ```py
        for box in boxes:
        ```
    - Create 3 variables from the data in the `box` list. And create a new variable called size that is a copy of box:
        ```py
        l, w, h = size = box
        ```
    - Remove the biggest size from the variable `size`:
        ```py
        size.remove(max(size))
        ```
    - Calculate the amount of `ribbon` needed for the `wrap` and the `bow`:
        ```py
        wrap = 2*(size[0] + size[1])
        bow = l * w * h
        ```
    - Add that to the total amount of `ribbon` needed:
        ```py
        ribbon += wrap + bow
        ```
    - Print and put the answer in the answer box:
        ```py
        print(ribbon)
        ```
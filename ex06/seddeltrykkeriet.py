#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    for i in range(len(widths)):
    	widths.append(heights[i])
    	heights.append(widths[i])
    	values.append(values[i])

    minne = [] #Dictionary for å lagre svar
    for k in range(paper_height + 1):
    	minne.append([0]*(paper_width + 1))

    for a in range(len(widths)):
    	if widths[a] > paper_width or heights[a] > paper_height:
    		continue

    	if values[a] > minne[heights[a]][widths[a]]:
    		minne[heights[a]][widths[a]] = values[a]

    minSeddel = min(widths)

    for y in range(minSeddel, paper_height + 1):
    	for x in range(minSeddel, paper_width + 1):
    		for i in range(x):
    			if  minne[y][i] + minne[y][x-i] > minne[y][x]:
    				minne[y][x] = minne[y][i] + minne[y][x-i]
    		for j in range(y):
    			if minne[j][x] + minne[y-j][x] > minne[y][x]:
    				minne[y][x] = minne[j][x] + minne[y-j][x]
    return minne[paper_height][paper_width]

def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()

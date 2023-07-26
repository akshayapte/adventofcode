import time


def simulate_sand(matrix, part):
	ans = 0
	length = len(matrix)
	
	while True:
		i, j = 0, 500
		while True:
			if i == length-1:
				break
			if matrix[i+1][j] == ".":
				i = i+1
			elif matrix[i+1][j-1] == ".":
				i = i+1
				j = j-1
			elif matrix[i+1][j+1] == ".":
				i = i+1
				j = j+1
			else:
				break

		if part == 1 and i == length-1:
			return ans
		elif part == 2 and matrix[0][500] == "O":
			return ans

		matrix[i][j] = "O"
		ans += 1 
		i, j = 0, 500


def draw_rock(matrix, coordinates):

	for i in range(len(coordinates)-1):
		start = [int(x) for x in coordinates[i]]
		end = [int(x) for x in coordinates[i+1]]

		if start[0] == end[0]:
			if end[1]>start[1]:
				for y in range(start[1], end[1]+1):
					matrix[y][start[0]] = "#"
			elif end[1]<start[1]:
				for y in range(end[1], start[1]+1):
					matrix[y][start[0]] = "#"

		elif start[1] == end[1]:
			if end[0]>start[0]:
				for x in range(start[0], end[0]+1):
					matrix[start[1]][x] = "#"
			elif end[0]<start[0]:
				for x in range(end[0], start[0]+1):
					matrix[start[1]][x] = "#"

	return matrix



def solve():
	with open("14.txt", "r") as inp:


		# part 1
		matrix = matrix = [ [ "." for i in range(1000) ] for j in range(1000) ]
		for line in inp.readlines():
			coordinates = [i.strip() for i in line.split(" -> ")]
			coordinates = [i.split(",") for i in coordinates]
			draw_rock(matrix, coordinates)
		
		ans1 = simulate_sand(matrix, part = 1)
		print(ans1)

		for x in range(0,1000):
			matrix[184][x] = "#"

		ans2 = simulate_sand(matrix, part = 2)
		print(ans1 + ans2)

		# Draws cave
		f = open("14_op.txt", "w")
		matrix = ["".join(i) for i in matrix]
		for line in matrix:
			f.write(line)
			f.write("\n")
		f.close()


if __name__ == "__main__":
	solve()
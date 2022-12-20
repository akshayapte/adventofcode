
def set_one(mat, x, y, rn):
	
	if rn%5 == 0:
		mat[(x,y)] = 1
		mat[(x+1,y)] = 1
		mat[(x+2,y)] = 1
		mat[(x+3,y)] = 1
	
	elif rn%5 == 1:
		mat[(x+1,y)] = 1
		mat[(x,y+1)] = 1
		mat[(x+1,y+1)] = 1
		mat[(x+2,y+1)] = 1
		mat[(x+1,y+2)] = 1
	
	elif rn%5 == 2:
		mat[(x,y)] = 1
		mat[(x+1,y)] = 1
		mat[(x+2,y)] = 1
		mat[(x+2,y+1)] = 1
		mat[(x+2,y+2)] = 1
	
	elif rn%5 == 3:
		mat[(x,y)] = 1
		mat[(x,y+1)] = 1
		mat[(x,y+2)] = 1
		mat[(x,y+3)] = 1
	
	elif rn%5 == 4:
		mat[(x,y)] = 1
		mat[(x+1,y)] = 1
		mat[(x+1,y+1)] = 1
		mat[(x,y+1)] = 1


def set_zero(mat, x, y, rn):
	
	if rn%5 == 0:
		mat[(x,y)] = 0
		mat[(x+1,y)] = 0
		mat[(x+2,y)] = 0
		mat[(x+3,y)] = 0
	
	elif rn%5 == 1:
		mat[(x+1,y)] = 0
		mat[(x,y+1)] = 0
		mat[(x+1,y+1)] = 0
		mat[(x+2,y+1)] = 0
		mat[(x+1,y+2)] = 0
	
	elif rn%5 == 2:
		mat[(x,y)] = 0
		mat[(x+1,y)] = 0
		mat[(x+2,y)] = 0
		mat[(x+2,y+1)] = 0
		mat[(x+2,y+2)] = 0
	
	elif rn%5 == 3:
		mat[(x,y)] = 0
		mat[(x,y+1)] = 0
		mat[(x,y+2)] = 0
		mat[(x,y+3)] = 0
	
	elif rn%5 == 4:
		mat[(x,y)] = 0
		mat[(x+1,y)] = 0
		mat[(x+1,y+1)] = 0
		mat[(x,y+1)] = 0

def can_move_down(mat, x, y, rn):
	if y <= 0:
		return None

	if rn%5 == 0:
		if mat.get((x,y-1),0) != 1 and mat.get((x+1,y-1),0) != 1 and mat.get((x+2,y-1),0) != 1 and mat.get((x+3,y-1),0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x,y-1)] = 1
			mat[(x+1,y-1)] = 1
			mat[(x+2,y-1)] = 1
			mat[(x+3,y-1)] = 1
			return (x, y-1)

	elif rn%5 == 1:
		if mat.get((x+1,y-1),0) != 1 and mat.get((x,y),0) != 1 and mat.get((x+2,y),0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1,y-1)] = 1
			mat[(x,y)] = 1
			mat[(x+1,y)] = 1
			mat[(x+2,y)] = 1
			mat[(x+1,y+1)] = 1
			return (x, y-1)

	elif rn%5 == 2:
		if mat.get((x,y-1),0) != 1 and mat.get((x+1,y-1),0) != 1 and mat.get((x+2,y-1),0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x,y-1)] = 1
			mat[(x+1,y-1)] = 1
			mat[(x+2,y-1)] = 1
			mat[(x+2,y)] = 1
			mat[(x+2,y+1)] = 1
			return (x, y-1)

	elif rn%5 == 3:
		if mat.get((x,y-1),0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x,y-1)] = 1
			mat[(x,y)] = 1
			mat[(x,y+1)] = 1
			mat[(x,y+2)] = 1
			return (x, y-1)

	elif rn%5 == 4:
		if mat.get((x,y-1),0) != 1 and mat.get((x+1,y-1),0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x,y-1)] = 1
			mat[(x+1,y-1)] = 1
			mat[(x+1,y)] = 1
			mat[(x,y)] = 1
			return (x, y-1)
	return None


def can_move_right(mat, x, y, rn):
	
	if rn%5 == 0:
		if x+4<7 and mat.get((x+4, y), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1,y)] = 1
			mat[(x+1+1,y)] = 1
			mat[(x+2+1,y)] = 1
			mat[(x+3+1,y)] = 1
			return (x+1, y)
	
	elif rn%5 == 1:
		if x+3<7 and mat.get((x+2, y), 0) != 1 and mat.get((x+3, y+1), 0) != 1 and mat.get((x+2, y+2), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1+1,y)] = 1
			mat[(x+1,y+1)] = 1
			mat[(x+1+1,y+1)] = 1
			mat[(x+1+2,y+1)] = 1
			mat[(x+1+1,y+2)] = 1
			return (x+1, y)
	
	elif rn%5 == 2:
		if x+3<7 and mat.get((x+3, y), 0) != 1 and mat.get((x+3, y+1), 0) != 1 and mat.get((x+3, y+2), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1,y)] = 1
			mat[(x+1+1,y)] = 1
			mat[(x+1+2,y)] = 1
			mat[(x+1+2,y+1)] = 1
			mat[(x+1+2,y+2)] = 1
			return (x+1, y)
	
	elif rn%5 == 3:
		if x+1<7 and mat.get((x+1, y), 0) != 1 and mat.get((x+1, y+1), 0) != 1 and mat.get((x+1, y+2), 0) != 1 and mat.get((x+1, y+3), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1,y)] = 1
			mat[(x+1,y+1)] = 1
			mat[(x+1,y+2)] = 1
			mat[(x+1,y+3)] = 1
			return (x+1, y)
	
	elif rn%5 == 4:
		if x+2<7 and mat.get((x+2, y), 0) != 1 and mat.get((x+2, y+1), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x+1,y)] = 1
			mat[(x+1+1,y)] = 1
			mat[(x+1+1,y+1)] = 1
			mat[(x+1,y+1)] = 1
			return (x+1, y)
	return None


def can_move_left(mat, x, y, rn):
	if x-1 < 0:
		return None
	
	if rn%5 == 0:
		if mat.get((x-1, y), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x-1,y)] = 1
			mat[(x+1-1,y)] = 1
			mat[(x+2-1,y)] = 1
			mat[(x+3-1,y)] = 1
			return (x-1,y)
	
	elif rn%5 == 1:
		if mat.get((x, y), 0) != 1 and mat.get((x-1, y+1), 0) != 1 and mat.get((x, y+2), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x-1+1,y)] = 1
			mat[(x-1,y+1)] = 1
			mat[(x-1+1,y+1)] = 1
			mat[(x-1+2,y+1)] = 1
			mat[(x-1+1,y+2)] = 1
			return (x-1,y)
	
	elif rn%5 == 2:
		if mat.get((x-1, y), 0) != 1 and mat.get((x+1, y+1), 0) != 1 and mat.get((x+1, y+2), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x-1,y)] = 1
			mat[(x-1+1,y)] = 1
			mat[(x-1+2,y)] = 1
			mat[(x-1+2,y+1)] = 1
			mat[(x-1+2,y+2)] = 1
			return (x-1,y)
	
	elif rn%5 == 3:
		if mat.get((x-1, y), 0) != 1 and mat.get((x-1, y+1), 0) != 1 and mat.get((x-1, y+2), 0) != 1 and mat.get((x-1, y+3), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x-1,y)] = 1
			mat[(x-1,y+1)] = 1
			mat[(x-1,y+2)] = 1
			mat[(x-1,y+3)] = 1
			return (x-1,y)
	
	elif rn%5 == 4:
		if mat.get((x-1, y), 0) != 1 and mat.get((x-1, y+1), 0) != 1:
			set_zero(mat, x,y, rn)
			mat[(x-1,y)] = 1
			mat[(x-1+1,y)] = 1
			mat[(x-1+1,y+1)] = 1
			mat[(x-1,y+1)] = 1
			return (x-1,y)
	return None


def give_mxht(x, y, rn):
	if rn%5 == 0:
		return y
	elif rn%5 == 1:
		return y+2
	elif rn%5 == 2:
		return y+2
	elif rn%5 == 3:
		return y+3
	elif rn%5 == 4:
		return y+1


def ppmt(mat):
	sss = ""
	for i in range(20):
		row = ""
		for j in range(7):
			row += str(mat.get((j, i), 0)) + " "
		sss += row[::-1] + "\n"
	print(sss)
	# pass


def part_one():
	
	matrix = {}
	f = open("17.txt", "r")
	inp = f.read()
	ctr = 0
	mxht = -1
	x = 2
	y = 3
	set_one(matrix, x, y, ctr)
	i=0
	
	while True:
		direction = inp[i]
		if direction == "<":
			op = can_move_left(matrix, x, y, ctr)
			if op:
				x = op[0]
				y = op[1]
		if direction == ">":
			op = can_move_right(matrix, x, y, ctr)
			if op:
				x = op[0]
				y = op[1]

		op = can_move_down(matrix, x, y, ctr)
		if op:
			x = op[0]
			y = op[1]
		else:
			mxht = max(mxht, give_mxht(x, y, ctr))
			ctr += 1
			x, y = 2, mxht+4
			set_one(matrix, x, y, ctr)
		if ctr == 2022:
			break
		i+=1
		if i == len(inp):
			i = 0

	print(mxht+1)

if __name__ == "__main__":
	part_one()
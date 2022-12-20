import time

def print_crt(ans: str):
	n=40
	chunks = [ans[i:i+n] for i in range(0, len(ans), n)]
	for chunk in chunks:
		print(chunk)


def part_one():
	with open("10.txt", "r") as inp:
		lines = inp.readlines()
		ctr = 0
		x = 1
		ans = 0
		marker = 20
		flag = False
		for tick in range(1, 240):
			if tick == marker:
				ans += tick*x
				marker += 40
			ins = lines[ctr].split(" ")
			if ins[0].strip() == "noop":
				ctr+=1
			elif ins[0].strip() == "addx":
				if not flag:
					flag = True
				elif flag:
					x += int(ins[1])
					ctr += 1
					flag = False
		print(ans)


def part_two():
	with open("10.txt", "r") as inp:
		lines = inp.readlines()
		ctr = 0
		x = 1
		ans = ""
		flag = False
		for tick in range(1, 241):
			draw = (tick-1)%40
			if abs(x-draw)<=1:
				ans += "#"
			else:
				ans += "."
			ins = lines[ctr].split(" ")
			if ins[0].strip() == "noop":
				ctr+=1
			elif ins[0].strip() == "addx":
				if not flag:
					flag = True
				elif flag:
					x += int(ins[1])
					ctr += 1
					flag = False
		print_crt(ans)

if __name__ == "__main__":
	part_one()
	part_two()



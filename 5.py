

def solution(crates: dict, part: int):
	with open("5.txt", "r") as inp:
		for line in inp.readlines():
			tokens = line.strip().split(" ")
			q = int(tokens[1])
			s = int(tokens[3])
			d = int(tokens[5])
			source_stack = crates[s]
			if part == 1:
				crates[d] = crates[d] + source_stack[-q:][::-1]
			if part == 2:
				crates[d] = crates[d] + source_stack[-q:]
			crates[s] = source_stack[0: -q]
		print("".join([i[-1] for i in crates.values()]))
		

if __name__ == "__main__":
	crates = {
		1: "MJCBFRLH",
		2: "ZCD",
		3: "HJFCNGW",
		4: "PJDMTSB",
		5: "NCDRJ",
		6: "WLDQPJGZ",
		7: "PZTFRH",
		8: "LVMG",
		9: "CBGPFQRJ"
	}
	solution(dict.copy(crates), part = 1)
	solution(dict.copy(crates), part = 2)
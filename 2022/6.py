def solution(marker: int):
	dic = {}
	with open("6.txt", "r") as inp:
		line = inp.read()
		for i,char in enumerate(line):
			if not dic.get(char):
				dic[char]=1
				if len(dic.keys()) == marker:
					print(i)
					break
			else:
				dic = {}

if __name__ == "__main__":
	solution(marker=4)
	solution(marker=13)
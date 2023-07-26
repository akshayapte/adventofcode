outcomes = {
	"A X":4,
	"A Y":8,
	"A Z":3,
	"B X":1,
	"B Y":5,
	"B Z":9,
	"C X":7,
	"C Y":2,
	"C Z":6
}

mappings = {
	"A X":"A Z",
	"A Y":"A X",
	"A Z":"A Y",
	"B X":"B X",
	"B Y":"B Y",
	"B Z":"B Z",
	"C X":"C Y",
	"C Y":"C Z",
	"C Z":"C X"
}

def part_one():
	with open("2.txt", "r") as inp:
		ans = 0
		lines = inp.readlines()
		for line in lines:
			ans += outcomes[line.strip()]
		print(ans)


def part_two():
	with open("2.txt", "r") as inp:
		ans = 0
		lines = inp.readlines()
		for line in lines:
			ans += outcomes[mappings[line.strip()]]
		print(ans)


if __name__ == "__main__":
	part_one()
	part_two()
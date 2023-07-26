from math import prod

def parse_monkey_data(lines: list):
	data = {}
	
	monkey_id = int(lines[0].split(" ")[1].strip(":"))	
	data["starting_items"] = [int(i.strip()) for i in lines[1].split(":")[1].split(",")]
	data["operation"] = lines[2].split(" = ")[1]
	data["test"] = int(lines[3].split(" ")[-1])
	data["true"] = int(lines[4].split(" ")[-1])
	data["false"] = int(lines[5].split(" ")[-1])
	data["inspections"] = 0
	
	return monkey_id, data

def eval_worry(old: int, operation: str, mod: int) -> int:
	operation.replace("old", str(old))
	return int(eval(operation))%mod

def solution(part: int, rounds: int):
	
	monkey_data = {}
	with open("11.txt", "r") as inp:
		monkey_lines = []
		for line in inp.readlines():
			if line == "\n":
				monkey_id, data = parse_monkey_data(monkey_lines)
				monkey_data[monkey_id] = data
				monkey_lines = []
			else:
				monkey_lines.append(line.strip())
		if monkey_lines:
			monkey_id, data = parse_monkey_data(monkey_lines)
			monkey_data[monkey_id] = data
			monkey_lines = []

	# product of all divisibility tests
	mod = prod([m["test"] for m in monkey_data.values()])

	for i in range(0,rounds):

		for monkey_id, data in monkey_data.items():
			for worry in data["starting_items"]:
				new_worry = eval_worry(worry, data["operation"], mod)
				if part == 1:
					new_worry = int(new_worry/3)

				if new_worry%data["test"] == 0:
					monkey_data[data["true"]]["starting_items"].append(new_worry)
				else:
					monkey_data[data["false"]]["starting_items"].append(new_worry)
				data["inspections"]+=1
			data["starting_items"] = []

	
	print(prod(sorted([i["inspections"] for i in monkey_data.values()])[-2:]))


if __name__ == "__main__":
	solution(part = 1, rounds = 20)
	solution(part = 2, rounds = 10000)
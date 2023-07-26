distances = {}
INF = 10000000

def score(valves, chosen_valves):
	ans = 0
	for chosen, time_left in chosen_valves.items():
		ans += time_left * valves[chosen]["flow"]
	return ans

def floyd_warshall(valves, rooms):
	for valve, data in valves.items():
		distances[(valve,valve)] = 0
		for nbr in data["tunnels"]:
			distances[(valve, nbr)] = 1

		for k in rooms:
			for i in rooms:
				for j in rooms:
					if distances.get((i,j), INF) > distances.get((i,k), INF) + distances.get((j,k), INF):
						distances[(i,j)] = distances.get((i,k), INF) + distances.get((j,k), INF)


def get_solutions(valves, time=30, chosen = {}, curr = "AA"):

	for nxt in valves:
		new_time = time - (distances.get((curr, nxt), INF) + 1)
		
		if new_time < 2:		
			continue

		new_chosen = chosen | {nxt: new_time}
		new_valves = valves - {nxt}

		yield from get_solutions(new_valves, new_time, new_chosen, nxt)

	yield chosen


def part_one():
	mx1, mx2 = 0, 0
	valves = {}
	with open("16.txt", "r") as inp:
		for line in inp.readlines():
			line = line.split(" ")
			valve = line[1]
			flow_rate = int(line[4].strip("rate=;"))
			tunnels = [i.strip(",\n") for i in line[9:]]
			valves[valve] = {}
			valves[valve]["flow"] = flow_rate
			valves[valve]["tunnels"] = tunnels
			rooms = valves.keys()
		
		floyd_warshall(valves, rooms)
		good_valves = [i for i in valves.keys() if valves[i]["flow"] != 0]
		
		# part 1
		for choice in get_solutions(set(good_valves)):
			mx1 = max(mx1, score(valves, choice))
		print(mx1)

		# part2 (Can be optimized)
		for c1 in get_solutions(set(good_valves), 26):
			for c2 in get_solutions(set(good_valves), 26):
				if not set(c1.keys()).intersection(set(c2.keys())):
					mx2 = max(mx2, score(valves, c1)+score(valves, c2))
		print(mx2)

		


if __name__ == "__main__":
	part_one()
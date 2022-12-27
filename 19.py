import json
import time

# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

def parse_input(blueprints, line):
	blueprint_id = int(line.split(" ")[1].strip(":"))
	ore_cost = {"ore": int(line.split(" ")[6])}
	clay_cost = {"ore": int(line.split(" ")[12])}
	obsidian_cost = {"ore": int(line.split(" ")[18]), "clay": int(line.split(" ")[21])}
	geode_cost = {"ore": int(line.split(" ")[-5]), "obsidian": int(line.split(" ")[-2])}
	blueprints[blueprint_id] = {
		"ore": ore_cost,
		"clay": clay_cost,
		"obsidian" : obsidian_cost,
		"geode": geode_cost
	}


def update_state(state):
	state["ore"] += state["ore_robot"]
	state["clay"] += state["clay_robot"]
	state["obsidian"] += state["obsidian_robot"]
	state["geode"] += state["geode_robot"]
	return state

def make_geode(geode_cost, state):
	state["ore"] -= geode_cost["ore"]
	state["obsidian"] -= geode_cost["obsidian"]
	state["geode_robot"] += 1
	return state
	
def make_obsidian(obsidian_cost, state):
	state["ore"] -= obsidian_cost["ore"]
	state["clay"] -= obsidian_cost["clay"]
	state["obsidian_robot"] += 1
	return state

def make_clay(clay_cost, state):
	state["ore"] -= clay_cost["ore"]
	state["clay_robot"] += 1
	return state

def make_ore(ore_cost, state):
	state["ore"] -= ore_cost["ore"]
	state["ore_robot"] += 1
	return state

def hash_dict(d):
	return json.dumps(d, sort_keys=True)


def bfs(blueprint_id, blueprint, state, time_limit = 24):
	visited = set()
	q = [state]
	scores = []
	best_geode_at = {}
	while q:

		curr = q.pop(0)
		if hash_dict(curr) in visited:
			continue

		visited.add(hash_dict(curr))
		curr["time"] += 1
		
		if curr["time"] > time_limit:
			scores.append(blueprint_id * curr["geode"])
			continue

		can_ore, can_clay, can_obsidian, can_geode = 0,0,0,0

		if curr["ore"] >= blueprint["ore"]["ore"]:
			can_ore = 1
		if curr["ore"] >= blueprint["clay"]["ore"]:
			can_clay = 1
		if curr["ore"] >= blueprint["obsidian"]["ore"] and curr["clay"] >= blueprint["obsidian"]["clay"]:
			can_obsidian = 1
		if curr["ore"] >= blueprint["geode"]["ore"] and curr["obsidian"] >= blueprint["geode"]["obsidian"]:
			can_geode = 1

		update_state(curr)

		if curr["geode"] < best_geode_at.get(curr["time"], 0):
			continue
		elif curr["geode"] > best_geode_at.get(curr["time"], 0):
			best_geode_at[curr["time"]] = curr["geode"]

		if can_geode:
			new_state = make_geode(blueprint["geode"], curr.copy())
			q.append(new_state)

		if can_obsidian and curr["obsidian_robot"] < blueprint["geode"]["obsidian"]:
			new_state = make_obsidian(blueprint["obsidian"], curr.copy())
			q.append(new_state)

		if can_clay and curr["clay_robot"] < blueprint["obsidian"]["clay"]:
			new_state = make_clay(blueprint["clay"], curr.copy())
			q.append(new_state)

		if can_ore and curr["ore_robot"] < max(blueprint["clay"]["ore"], blueprint["obsidian"]["ore"], blueprint["geode"]["ore"]):
			new_state = make_ore(blueprint["ore"], curr.copy())
			q.append(new_state)

		q.append(curr)

	return max(scores)


def main():
	ans = 0
	with open("19.txt", "r") as inp:
		blueprints = {}
		for line in inp.readlines():
			parse_input(blueprints, line)


	for blueprint_id, blueprint in blueprints.items():
		state = {
		 "ore": 0,
		 "clay": 0,
		 "obsidian": 0,
		 "geode": 0,
		 "ore_robot":1,
		 "clay_robot":0,
		 "obsidian_robot":0,
		 "geode_robot":0,
		 "time": 0
		}
		quality = bfs(blueprint_id, blueprint, state)
		ans += quality

	print(ans)
		

if __name__ == '__main__':
	main()
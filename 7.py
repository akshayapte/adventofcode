import time
sizes = {}

def nested_set(dic, keys, value):
	for key in keys[:-1]:
		dic = dic.setdefault(key, {})
	dic[keys[-1]] = value

def iterdict(d):
	global sizes
	sm = 0
	for k,v in d.items():
		if isinstance(v, dict):
			sm += iterdict(v)
		else:
			sm += v
	sizes[str(d)] = sm
	return sm


if __name__ == "__main__":

	with open("7.txt", "r") as inp:
		tree = {}
		ans = 0
		path = []
		current_space = 0
		for line in inp.readlines():
			token = [i.strip() for i in line.split(" ")]
			if token[1]=="cd":
				if token[2]=="..":
					path.pop()
				elif token[2]=="/":
					path = ["/"]
				else:
					path.append(token[2])
			elif token[1] == "ls":
				continue
			elif token[0] == "dir":
				nested_set(tree, path + [token[1]], {})
				continue
			else:
				nested_set(tree, path + [token[1]] , int(token[0]))
				current_space += int(token[0])
		iterdict(tree)

		# Part 1
		for k,v in sizes.items():
			if v<=100000:
				ans += v
		print(ans)

		# Part 2
		v = (sorted(list(sizes.values())))
		available_space = 70000000 - current_space
		freeable_space = 30000000 - available_space
		for size in v:
			if int(size)>=freeable_space:
				print(size)
				break

OFFSETS = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDES = {"1x":1, "1y":1, "1z":1, "-1x":1, "-1y":1, "-1z":1}
MAXX, MAXY, MAXZ = -1,-1,-1

def find_blocked_face(cube1, cube2):

	if cube1[0] == cube2[0] and cube1[1] == cube2[1] and abs(cube1[2] - cube2[2]) == 1:
		return str(cube1[2] - cube2[2]) + "z"
	if cube1[0] == cube2[0] and abs(cube1[1] - cube2[1]) == 1 and cube1[2] == cube2[2]:
		return str(cube1[1] - cube2[1]) + "y"
	if abs(cube1[0] - cube2[0]) == 1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]:
		return str(cube1[0] - cube2[0]) + "x"
	return None


def bfs(start, air_map, cubes_map):
	queue = [start]
	v = {start}
	while queue:
		cube = queue.pop()
		air_map.add(cube)
		for offset in OFFSETS:
			new = (tuple([sum(i) for i in list(zip(cube, offset))]))
			if new not in v:
				v.add(new)
				if new[0] >= 0 and new[0] <= MAXX + 1 and new[1] >= 0 and new[1] <= MAXY + 1 and new[2] >= 0 and new[2] <= MAXZ + 1 \
					and new not in cubes_map and new not in air_map:
					queue.append(new)




def solve():

	with open("18.txt", "r") as inp:
		global MAXX, MAXY, MAXZ
		cubes = []
		cubes_map = {}
		i,j = 0,0
		air_map = set()
		for line in inp.readlines():
			x,y,z = [int(i) for i in line.split(",")]

			MAXX = max(MAXX, x)
			MAXY = max(MAXY, y)
			MAXZ = max(MAXZ, z)
			cubes.append((x,y,z))
			cubes_map[(x,y,z)] = 6

		l = len(cubes)
		

		# part 1
		for i in range(l):
			dic = SIDES.copy()
			for j in range(l):
				if i != j:
					blocked = find_blocked_face(cubes[i], cubes[j])
					if(blocked):
						if dic[blocked] == 1:
							cubes_map[cubes[i]] = max(cubes_map[cubes[i]]-1, 0)
							dic[blocked] = 0

		ans1 = sum(cubes_map.values())
		print(ans1)

		bfs((0,0,0), air_map, cubes_map)

		# find air pockets inside obsidian block
		air_pockets = {}
		for i in range(MAXX + 1):
			for j in range(MAXY + 1):
				for k in range(MAXZ + 1):
					if (i,j,k) not in cubes_map and (i,j,k) not in air_map:
						air_pockets[(i,j,k)] = 6
		

		for ap1 in air_pockets.keys():
			dic = SIDES.copy()
			for ap2 in air_pockets.keys():
				if ap1!= ap2:
					blocked = find_blocked_face(ap1, ap2)
					if(blocked):
						if dic[blocked] == 1:
							air_pockets[ap1] = max(air_pockets[ap1]-1, 0)
							dic[blocked] = 0

		ans2 = ans1 - sum(air_pockets.values())
		print(ans2)

if __name__ == "__main__":
	solve()
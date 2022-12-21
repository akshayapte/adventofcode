
def find_blocked_face(cube1, cube2):
	if cube1[0] == cube2[0] and cube1[1] == cube2[1] and abs(cube1[2] - cube2[2]) == 1:
		return str(cube1[2] - cube2[2]) + "z"
	if cube1[0] == cube2[0] and abs(cube1[1] - cube2[1]) == 1 and cube1[2] == cube2[2]:
		return str(cube1[1] - cube2[1]) + "y"
	if abs(cube1[0] - cube2[0]) == 1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]:
		return str(cube1[0] - cube2[0]) + "x"
	return None

def solve():

	with open("18.txt", "r") as inp:
		cubes = []
		i,j,ans = 0,0,0
		for line in inp.readlines():
			x,y,z = [int(i) for i in line.split(",")]
			cubes.append((x,y,z))
		l = len(cubes)
		
		for i in range(l):

			dic = {
			"1x":1,
			"1y":1,
			"1z":1,
			"-1x":1,
			"-1y":1,
			"-1z":1,
			}

			for j in range(l):
				if i != j:
					blocked = find_blocked_face(cubes[i], cubes[j])
					if(blocked):
						dic[blocked] = 0


			ans += sum(dic.values())
		
		print(ans)

if __name__ == "__main__":
	solve()
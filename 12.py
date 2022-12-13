
import time
INF = 100000000000


def get_ord(x: str):
	if x == "S":
		return ord("a")
	elif x == "E":
		return ord("z")
	return ord(x)

def get_edges(matrix: list[list], i: int, j: int):
	edges = []
	curr_val = get_ord(matrix[i][j])
	length = len(matrix)
	width = len(matrix[0])

	if i>0 and get_ord(matrix[i-1][j])-curr_val<=1:
		edges.append((i-1,j))
	if i<length-1 and get_ord(matrix[i+1][j])-curr_val<=1:
		edges.append((i+1,j))
	if j<width-1 and get_ord(matrix[i][j+1])-curr_val<=1:
		edges.append((i,j+1))
	if j>0 and get_ord(matrix[i][j-1])-curr_val<=1:
		edges.append((i,j-1))
	
	return edges


def dijkstra(ad_list, S, E):

	distance = {}
	distance[S] = 0
	queue = []
	queue.append((S, 0))

	while len(queue)>0:
		node, cost = queue.pop()
		if distance[node] != cost:
			continue

		for edge in ad_list[node]:
			if(distance.get(edge, INF) > cost + 1):
				distance[edge] = cost + 1
				queue.append((edge, cost + 1))

	return distance



def solve():
	with open("12.txt", "r") as inp:

		#  part 1
		ad_list = {}
		matrix = [list(i.strip()) for i in inp.readlines()]
		mn = INF
		length = len(matrix)
		width = len(matrix[0])
		for i in range(0,length):
			for j in range(0, width):
				if matrix[i][j] == "S":
					S = (i,j)
				if matrix[i][j] == "E":
					E = (i,j)
				ad_list[(i,j)] = get_edges(matrix, i, j)
		
		distances = dijkstra(ad_list, S, E)
		print(distances[E])


		# part 2
		# TODO: Find a better way instead of running Dijkstra on every starting node.
		for i in range(0,length):
			for j in range(0, width):
				if matrix[i][j] == "S" or matrix[i][j] == "a":
					S = (i,j)
					distances = dijkstra(ad_list, S, E)
					mn = min(mn, distances.get(E, INF))
		print(mn)



if __name__ == "__main__":
	solve()
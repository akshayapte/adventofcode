def update_tail(h,t):
	if h[0]-t[0]>1 and h[1]==t[1]:
		return(t[0]+1, t[1])
	elif h[1]-t[1]>1 and h[0]==t[0]:
		return(t[0], t[1]+1)
	elif t[0]-h[0]>1 and h[1]==t[1]:
		return(t[0]-1, t[1])
	elif t[1]-h[1]>1 and h[0]==t[0]:
		return(t[0], t[1]-1)

	# x,y 
	elif h[0]-t[0]>=1 and h[1]-t[1]>1:
		return(t[0]+1, t[1]+1)
	elif h[0]-t[0]>1 and h[1]-t[1]>=1:
		return(t[0]+1, t[1]+1)

	# x,-y
	elif h[0]-t[0]>=1 and t[1]-h[1]>1:
		return(t[0]+1, t[1]-1)
	elif h[0]-t[0]>1 and t[1]-h[1]>=1:
		return(t[0]+1, t[1]-1)

	# -x,y	 
	elif t[0]-h[0]>=1 and h[1]-t[1]>1:
		return(t[0]-1, t[1]+1)
	elif t[0]-h[0]>1 and h[1]-t[1]>=1:
		return(t[0]-1, t[1]+1)

	# -x,-y
	elif t[0]-h[0]>=1 and t[1]-h[1]>1:
		return(t[0]-1, t[1]-1)
	elif t[0]-h[0]>1 and t[1]-h[1]>=1:
		return(t[0]-1, t[1]-1)
	else:
		return t

def solve(knots: int):
	with open("9.txt", "r") as inp:

		directions = ""
		visited=set()
		for line in inp.readlines():
			line = line.split(" ")
			directions += line[0]*int(line[1].strip())
		pos = [[0,0]]*knots

		for direction in directions:
			if direction=="R":
				pos[0][0]+=1
			elif direction=="L":
				pos[0][0]-=1
			elif direction=="U":
				pos[0][1]+=1
			elif direction=="D":
				pos[0][1]-=1

			
			for i in range(1,knots):
				pos[i] = list(update_tail(pos[i-1],pos[i]))
			
			visited.add(tuple(pos[knots-1]))
		print(len(visited))


if __name__ == "__main__":
	solve(2)
	solve(10)


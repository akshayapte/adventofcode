def part_one():
	with open("4.txt", "r") as inp:
		lines = inp.readlines()
		ans = 0
		for line in lines:

			set1 = [int(i) for i in line.split(",")[0].split("-")]
			set2 = [int(i) for i in line.split(",")[1].split("-")]
			size1 = abs(set1[0]-set1[1])
			size2 = abs(set2[0]-set2[1])
			
			if size1>size2:
				if set1[0]<=set2[0] and set1[1]>=set2[1]:
					ans+=1
					
			elif size1<size2:
				if set2[0]<=set1[0] and set2[1]>=set1[1]:
					ans+=1
					
			elif size1==size2:
				if set1 == set2:
					ans+=1
					
		print(ans)

def part_two():
	with open("4.txt", "r") as inp:
		lines = inp.readlines()
		ans = 0
		for line in lines:

			set1 = [int(i) for i in line.split(",")[0].split("-")]
			set2 = [int(i) for i in line.split(",")[1].split("-")]

			if max(set1[0], set2[0]) <= min(set1[1], set2[1]):
				ans+=1
		print(ans)

if __name__ == "__main__":
	part_one()
	part_two()
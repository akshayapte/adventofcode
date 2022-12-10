
class PriorityQueue(object):
	def __init__(self):
		self.queue = []
 
	def sum(self):
		return sum(self.queue)

	def length(self):
		return len(self.queue)
 
	def insert(self, data):
		self.queue.append(data)
 
	def delete(self):
		try:
			max_val = 0
			for i in range(len(self.queue)):
				if self.queue[i] < self.queue[max_val]:
					max_val = i
			item = self.queue[max_val]
			del self.queue[max_val]
			return item
		except IndexError:
			print()
			exit()

def part_one():
	with open("1.txt", "r") as inp:
		mx = 0
		lines = inp.readlines()
		curr = 0
		for line in lines:
			if line == "\n":
				mx = max(curr, mx)
				curr=0
			else:
				curr+=int(line)
				
		print(mx)

def part_two():
	with open("1.txt", "r") as inp:
		q = PriorityQueue()
		mx = 0
		lines = inp.readlines()
		curr = 0
		for line in lines:
			if line == "\n":
				q.insert(curr)
				if q.length()>3:
					q.delete()
				curr=0
			else:
				curr+=int(line)
				
		print(q.sum())

if __name__ == "__main__":
	part_one()
	part_two()
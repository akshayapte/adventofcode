
positions = {}
inverse = {}

def move_left(key, l):
	places = abs(key[0])%l
	current_pos = positions[key]

	if places <= current_pos:
		new_pos = current_pos - places
	else:
		new_pos = l - (places - current_pos)
	
	for i in range(new_pos, l-2):
		inverse[i+1] = inverse[i]
		positions[inverse[i]] = i+1
		
	positions[key] = new_pos
	inverse[new_pos] = key

def move_right(key, l):
	places = key[0]%l
	current_pos = positions[key]

	if places + current_pos <= (l - 1):
		new_pos = current_pos + places #2
	else:
		new_pos = (current_pos+places) - l

	for i in range(current_pos, new_pos+1):
		inverse[i] = inverse[i+1]
		positions[inverse[i+1]] = i

	positions[key] = new_pos
	inverse[new_pos] = key




def main():
	with open("20.txt", "r") as inp:
		nums = inp.readlines()
		l = len(nums)
		for i,num in enumerate(nums):
			num = int(num.strip("\n"))
			positions[(num, i)] = i
			inverse[i] = (num, i)
		for i,num in enumerate(nums):
			num = int(num.strip("\n"))
			if num<0:
				move_left((num, i), l)
			elif num>0:
				move_right((num,i), l)
			print([i.strip("\n") for i in nums],"\n",inverse,"\n", positions,"\n\n")

if __name__ == '__main__':
	main()



# ,currpos = 4 ,places = 3 ,l = 5. new_pos = 
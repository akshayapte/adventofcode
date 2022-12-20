from collections import Counter
def find_common_chars(str1,str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)
 
    commonDict = dict1 & dict2
 
    if len(commonDict) == 0:
        print (-1)
        return

    commonChars = list(commonDict.elements()) 
    commonChars = sorted(commonChars)
 
    return(''.join(commonChars))


def find_common(line, l):
	mid = int(l/2)
	for char1 in range(0,mid):
		for char2 in range(mid, l):
			if line[char1] == line[char2]:
				return line[char1]


def part_one():
	with open("3.txt","r") as inp:
		ans = 0
		lines = inp.readlines()
		i=0
		for line in lines:
			common = find_common(line, len(line))
			if len(common)>1:
				common = common[0]
			if common.islower():
				ans+= ord(common)-96
			elif common.isupper():
				ans+= ord(common)-38
		print(ans)


def part_two():
	with open("3.txt","r") as inp:
		ans = 0
		lines = inp.readlines()
		i=0
		while(i<300):
			common = find_common_chars(find_common_chars(lines[i].strip(), lines[i+1].strip()), lines[i+2].strip())
			i+=3
			if len(common)>1:
				common = common[0]
			if common.islower():
				ans+= ord(common)-96
			elif common.isupper():
				ans+= ord(common)-38
		print(ans)

if __name__ == "__main__":
	part_one()
	part_two()
import json


def in_order(p1, p2):
	for i in range(min(len(p1), len(p2))):
		
		# int int
		if type(p1[i]) == int and type(p2[i]) == int:
			if p1[i]==p2[i]:
				continue
			return p1[i]<p2[i]

		# one int one list
		if type(p1[i]) == int or type(p2[i]) == int:
			if type(p1[i]) == int:
				ret = in_order([p1[i]], p2[i])
			elif type(p2[i]) == int:
				ret = in_order(p1[i], [p2[i]])
			if ret is None:
				continue
			return ret

		# both lists
		if type(p1[i]) == list and type(p2[i]) == list:
			ret = in_order(p1[i], p2[i])
			if ret is None:
				continue
			return ret

	if len(p1) != len(p2):
		return len(p1) < len(p2)


def part_one():
	with open("13.txt", "r") as inp:
		packet_pairs = inp.read().split("\n\n")
		ans = 0
		for i, packet_pair in enumerate(packet_pairs):
			packet_pair = packet_pair.split("\n")
			packet1 = json.loads(packet_pair[0].strip())
			packet2 = json.loads(packet_pair[1].strip())
			if in_order(packet1, packet2):
				ans += i+1

	print(ans)

def part_two():
	with open("13.txt", "r") as inp:
		packets = []
		for packet in inp.readlines():
			if packet == "\n":
				continue
			else:
				packets.append(json.loads(packet.strip()))

		index1 = 1
		index2 = 1

		for packet in packets:
			if in_order(packet, [[2]]):
				index1 += 1

		packets.append([[2]])

		for packet in packets:
			if in_order(packet, [[6]]):
				index2 += 1

		print(index1*index2)


if __name__ == "__main__":
	part_one()
	part_two()

def manhattan_distance(a,b):
    return abs(a[0]- b[0]) + abs(a[1]-b[1])

def coordinates(a, dist, _y):
    x1 = a[0] + (dist - abs(a[1] - _y))
    x2 = a[0] - (dist - abs(a[1] - _y))
    return (x1,x2)
    

def parse_input(line, sensor_data):
    segments = line.split(" ")
    x1 = int(segments[2].strip(",").split("=")[-1])
    y1 = int(segments[3].strip(":").split("=")[-1])

    x2 = int(segments[8].strip(",").split("=")[-1])
    y2 = int(segments[-1].split("=")[-1])

    sensor_data[(x1,y1)] = (x2,y2)


def part_one():
    sensor_data = {}
    distances = {}
    with open("15.txt", "r") as inp:
        for line in inp.readlines():
            parse_input(line, sensor_data)

    beacons = sensor_data.values()
    
    for sensor, beacon in sensor_data.items():
        distances[sensor] = manhattan_distance(sensor, beacon)
    
    
    visited = set()
    _y = 2000000

    for sensor,distance in distances.items():
        
        if manhattan_distance(sensor, (sensor[0],_y)) <= distance:
            x1,x2 = coordinates(sensor, distance, _y)
            for i in range(min(x1,x2), max(x1,x2)+1):
                if (i,_y) not in beacons:
                    visited.add((i, _y))

    print(len(visited))


if __name__ == "__main__":
    part_one()
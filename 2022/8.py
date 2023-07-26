if __name__ == "__main__":
    
    input = open('8.txt').read().strip().splitlines()
    height = len(input)
    width = len(input[0])
    visible = set()
    scenic = 0

    for y in range(height):
        for x in range(width):
            score = 1
            tree = input[y][x]
            left = input[y][:x][::-1]
            right = input[y][x+1:width]
            up = [input[ny][x] for ny in reversed(range(y))]
            down = [input[ny][x] for ny in range(y+1,height)]
            
            for direction in left, down, up, right:
                for i, neighbour in enumerate(direction):
                    if tree <= neighbour:
                        score *= i+1
                        break
                else:
                    score *= len(direction)
                    visible.add((y,x))
            scenic = max(scenic, score)

    print(len(visible))
    print(scenic)
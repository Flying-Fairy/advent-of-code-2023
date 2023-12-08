instructions = ""
network = {}

with open("inputs/input8.txt") as f:
    for line in f.readlines():
        line = line.strip()
        
        if line.endswith(("L", "R")):
            instructions = line
        
        elif "=" in line:
            line = line.split()
            node, directions = line[0], line[2:]
            direction = (directions[0][1:-1], directions[1][:-1])
            network[node] = direction

start = "AAA"
END = "ZZZ"
moves = 0

while start != END:
    for dest in instructions:
        moves += 1 
        if dest == "L":
            start = network[start][0]
        elif dest == "R":
            start = network[start][1]
        
        if start == END:
            print("part 1:", moves)
            break
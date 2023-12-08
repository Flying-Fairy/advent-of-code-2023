from math import lcm

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

starts = [s for s in network.keys() if s.endswith("A")]
ends = []

for start in starts:
    moves = 0    
    
    while not start.endswith("Z"):
        for dest in instructions:
            moves += 1
            if dest == "L":
                start = network[start][0]
            elif dest == "R":
                start = network[start][1]
                    
            if start.endswith("Z"):
                ends.append(moves)
                break 

print(lcm(*ends))
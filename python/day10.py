pipe_map = []

with open("inputs/input10.txt") as f:
    for line in f.readlines():
        pipe_map.append(line.strip())

for r_index, row in enumerate(pipe_map):
    for c_index, col in enumerate(row):
        if col == "S":
            start_pos = (r_index, c_index)
            
traversed = {start_pos}
queue = [start_pos]
start_tile = {"|", "J", "L", "-", "F", "7"}

while queue:
    x, y = queue.pop(0)
    tile = pipe_map[x][y]
    
    if x > 0 and tile in "S|JL" and pipe_map[x - 1][y] in "F7|":
        if (x - 1, y) not in traversed:
            queue.append((x - 1, y))
            traversed.add((x - 1, y))
            if tile == "S":
                start_tile = start_tile & set("|JL")
        
    if x < (len(pipe_map) - 1) and tile in "S|F7" and pipe_map[x + 1][y] in "|JL":
        if (x + 1, y) not in traversed:
            queue.append((x + 1, y))
            traversed.add((x + 1, y))
            if tile == "S":
                start_tile = start_tile & set("|F7")
        
    if y > 0 and tile in "S-J7" and pipe_map[x][y - 1] in "-LF":
        if (x, y - 1) not in traversed:
            queue.append((x, y - 1))
            traversed.add((x, y - 1))
            if tile == "S":
                start_tile = start_tile & set("-J7")
        
    if y < (len(pipe_map[0]) - 1) and tile in "S-LF" and pipe_map[x][y + 1] in "-J7":
        if (x, y + 1) not in traversed:
            queue.append((x, y + 1))
            traversed.add((x, y + 1))
            if tile == "S":
                start_tile = start_tile & set("-LF")
        
print(len(traversed) // 2)
start_tile = start_tile.pop()

pipe_map = [row.replace("S", start_tile) for row in pipe_map]
pipe_map = ["".join(c if (ri, ci) in traversed else "." for ci, c in enumerate(r)) for ri, r in enumerate(pipe_map)]

total = 0 

for row in pipe_map:
    inside = False
    ps = None
    
    for char in row:
        if char == "|":
            inside = not inside
        
        elif char in "FL":
            ps = char
        
        elif char == "J":
            if ps == "L":
                ps = None
            else:
                inside = not inside
                ps = None
        
        elif char == "7":
            if ps == "F":
                ps == None
            else:
                inside = not inside
                ps = None
        
        elif char == "." and inside:
            total += 1

print(total)
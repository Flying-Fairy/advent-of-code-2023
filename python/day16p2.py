data = open("inputs/input16.txt").read().split("\n")

start_up = [(-1, i, 1, 0) for i in range(len(data[0]))]
start_left = [(i, -1, 0, 1) for i in range(len(data))]
start_right = [(i, len(data[0]), 0, -1) for i in range(len(data))]
start_down = [(len(data), i, -1, 0) for i in range(len(data[0]))]

all_starts = start_up + start_right + start_left + start_down

def lava_check(start):
    queue = [start]
    visited = set()
    
    while queue:
        x, y, dx, dy = queue.pop(0)
        x, y = x + dx, y + dy
        
        if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]):
            continue
        
        char = data[x][y]
        
        if char == "." or (char == "-" and dy != 0) or (char == "|" and dx != 0):
            if (x, y, dx, dy) not in visited:
                queue.append((x, y, dx, dy))
                visited.add((x, y, dx, dy))
        
        elif char == "\\":
            if dy != 0:
                if dy > 0:
                    if (x, y, 1, 0) not in visited:
                        queue.append((x, y, 1, 0))
                        visited.add((x, y, 1, 0))
                else:
                    if (x, y, -1, 0) not in visited:
                        queue.append((x, y, -1, 0))
                        visited.add((x, y, -1, 0))
            
            elif dx != 0:
                if dx > 0:
                    if (x, y, 0, 1) not in visited:
                        queue.append((x, y, 0, 1))
                        visited.add((x, y, 0, 1))
                else:
                    if (x, y, 0, -1) not in visited:
                        queue.append((x, y, 0, -1))
                        visited.add((x, y, 0, -1))
                        
        elif char == "/":
            if dy != 0:
                if dy > 0:
                    if (x, y, -1, 0) not in visited:
                        queue.append((x, y, -1, 0))
                        visited.add((x, y, -1, 0))
                else:
                    if (x, y, 1, 0) not in visited:
                        queue.append((x, y, 1, 0))
                        visited.add((x, y, 1, 0))
            
            elif dx != 0:
                if dx > 0:
                    if (x, y, 0, -1) not in visited:
                        queue.append((x, y, 0, -1))
                        visited.add((x, y, 0, -1))
                else:
                    if (x, y, 0, 1) not in visited:
                        queue.append((x, y, 0, 1))
                        visited.add((x, y, 0, 1))

        elif char == "|" and dy != 0:
            if x - 1 >= 0:
                queue.append((x, y, -1, 0))
                visited.add((x, y, -1, 0))
            if x + 1 < len(data):
                queue.append((x, y, 1, 0))
                visited.add((x, y, 1, 0))

        elif char == "-" and dx != 0:
            if y - 1 >= 0:
                queue.append((x, y, 0, -1))
                visited.add((x, y, 0, -1))
            if y + 1 < len(data[0]):
                queue.append((x, y, 0, 1))
                visited.add((x, y, 0, 1))

    return len({d[:2] for d in visited})

max_energy = 0

for s in all_starts:
    result = lava_check(s)
    if result > max_energy:
        max_energy = result

print(max_energy)

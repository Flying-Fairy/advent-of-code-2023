from collections import defaultdict

total_1 = 0
total_2 = 0
gear_pos = defaultdict(list)

def check_neighbors(pos, grid):
    x, y = pos
    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (0, -1)]
    for d in directions:
        dx, dy = x + d[0], y + d[1]
        try:
            if not grid[dx][dy].isdigit() and grid[dx][dy] != ".":
                return True, (dx, dy)
        except IndexError:
            continue
    return False, None

with open("inputs/input3.txt") as f:
    schematic_engine = [line.strip() for line in f.readlines()]

for x, row in enumerate(schematic_engine):
    curr_num = ""
    adjacent = False
    gear = None
    
    for y, col in enumerate(row):
        pos = (x, y) 
        
        if col.isdigit():
            curr_num += col
            if not adjacent:
                adjacent, gear = check_neighbors(pos, schematic_engine)            
        
        if not col.isdigit() or y >= len(row) - 1: 
            if adjacent:
                total_1 += int(curr_num)
                adjacent = False
            if gear and schematic_engine[gear[0]][gear[1]] == "*":
                gear_pos[gear].append(int(curr_num))
                gear = None
            
            curr_num = ""

for gear_pair in gear_pos.values():
    if len(gear_pair) == 2:
        total_2 += gear_pair[0] * gear_pair[1]
      
print("part 1:", total_1)
print("part 1:", total_2)
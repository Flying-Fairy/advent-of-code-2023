galaxy_map = []
empty_rows = []
empty_cols = []
total = 0 
exp_size = 1000000 - 1 # size is 1 for part 1.

with open("inputs/input11.txt") as f:
    for i, line in enumerate(f.readlines()):
        galaxy_map.append(list(line.strip()))
        if "#" not in line:
            empty_rows.append(i)

for i, col in enumerate(zip(*galaxy_map)):
    if all(c == "." for c in col):
        empty_cols.append(i)

galaxies = []

for r_index, row in enumerate(galaxy_map):
    for c_index, col in enumerate(row):
        if col == "#":
            galaxies.append((r_index, c_index))
     
while len(galaxies) > 1:
    x, y = galaxies.pop(0)
    for g in galaxies:
        diff = 0
        for row_index in empty_rows:
            if x < row_index < g[0] or x > row_index > g[0]:
                diff += exp_size
        for col_index in empty_cols:
            if y < col_index < g[1] or y > col_index > g[1]:
                diff += exp_size
        
        total += ((abs(x - g[0])) + (abs(y - g[1]))) + diff

print(total)
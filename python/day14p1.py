data = list(map(list, open("inputs/input14.txt").read().split("\n")))


def fall_rock(pos, grid):
    x, y = pos
    if grid[x][y] in "O#":
        return (x + 1, y)
    elif x == 0:
        return pos
    else:
        return fall_rock((x - 1, y), grid)


for row_index, row in enumerate(data):
    for col_index, col in enumerate(row):
        if col == "O" and row_index > 0:
            x, y = fall_rock((row_index - 1, col_index), data)
            data[row_index][col_index], data[x][y] = data[x][y], data[row_index][col_index]
    
total = 0
    
for i, load in enumerate(data):
    total += load.count("O") * (len(data) - i)
    
print(total)
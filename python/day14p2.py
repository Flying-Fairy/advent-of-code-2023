from copy import deepcopy

data = list(map(list, open("inputs/input14.txt").read().split("\n")))


def fall_north(pos, grid):
    x, y = pos
    if x == 0:
        return pos
    if grid[x - 1][y] in "O#":
        return (x, y)
    else:
        return fall_north((x - 1, y), grid)
    

def fall_west(pos, grid):
    x, y = pos
    if y == 0:
        return pos
    if grid[x][y - 1] in "O#":
        return (x, y)
    else:
        return fall_west((x, y - 1), grid)


def count_load(grid):
    total = 0
    for i, load in enumerate(grid):
        total += load.count("O") * (len(grid) - i) 
    
    return total   


def grid_fall(grid, fall_func):    
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == "O":
                x, y = fall_func((row_index, col_index), grid)
                grid[row_index][col_index], grid[x][y] = grid[x][y], grid[row_index][col_index]

    return grid


def cycle(grid):
    north = grid_fall(grid, fall_north)
    west = grid_fall(north, fall_west)
    south = grid_fall(west[::-1], fall_north)
    east = grid_fall([d[::-1] for d in south[::-1]], fall_west)
    
    return [d[::-1] for d in east]


cycles_list = []
n = 0
cycle_start = 0

while True:
    n += 1
    data = cycle(data)
    if data in cycles_list:
        cycle_start = cycles_list.index(data) + 1
        break
    
    cycles_list.append(deepcopy(data))
    
result = ((1000000000 - cycle_start) % (n - cycle_start)) + cycle_start
print(count_load(cycles_list[result - 1]))
data = open("inputs/input13.txt").read().split("\n\n")

def is_mirrored(l, r):
    for left, right in zip(l, r):
        if left != right:
            return False
    return True


def check_grid(grid):
        for i in range(len(grid) - 1):
            if grid[i] == grid[i + 1]:
                left = grid[:i + 1]
                right = grid[i + 1:]
                
                mirrored = is_mirrored(left[::-1], right)
                
                if mirrored:
                    return i + 1


def get_mirror_index(grid):    
    horizon = grid.split("\n")
    vertical = list(zip(*horizon))
    
    h_value = check_grid(horizon)
    if h_value != None:
        return ("H", h_value)
    
    v_value = check_grid(vertical)
    if v_value != None:
        return ("V", v_value)
    

total = 0

for d in data:
    score = 0
    dirr, index = get_mirror_index(d)
    
    if dirr == "V":
        score += index
    else:
        score += index * 100
    
    total += score

print(total)
        
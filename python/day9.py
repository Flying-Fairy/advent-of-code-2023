data = open("inputs/input9.txt").read().splitlines()
steps = []

for row in data:
    row = list(map(int, row.split()))[::-1] # remove reverse for part 1.
    temp = [row]
    
    while not all(x == 0 for x in row):
        new_row = []
        
        for i in range(0, len(row) - 1):
            new_row.append((row[i + 1] - row[i]))
        
        row = new_row
        temp.append(new_row)
    
    steps.append(temp)

total_list = []

for step in steps:
    total = 0
    
    for s in step[::-1]:
        total += s[-1]
    
    total_list.append(total)

print(sum(total_list))
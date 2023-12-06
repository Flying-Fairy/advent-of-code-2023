seed_map = []

with open("inputs/input5.txt") as f:
    temp_list = []
    for line in f.readlines():
        if line == "\n":
            seed_map.append(temp_list)
            temp_list = []
        else:
            temp_list.append(line.strip())
    seed_map.append(temp_list)

seeds = list(map(int, seed_map.pop(0)[0].split()[1:]))
lowest_loc = float("inf")
       
for seed in seeds:
    for row in seed_map:
        seed_nums = []
        for num_seed in row[1:]:
            seed_nums.append(list(map(int, num_seed.split())))                
        
        for dest, source, length in seed_nums:
            max_range = source + length
              
            if source <= seed < max_range:
                seed = seed - source + dest 
                break
    
    if seed < lowest_loc:
        lowest_loc = seed

print("part 1:", lowest_loc)

seed_ranges = []

for n in range(0, len(seeds), 2):
    start, r = seeds[n], seeds[n + 1]
    seed_ranges.append((start, start + r))
  
for row in seed_map:
    seed_nums = []
    for num_seed in row[1:]:
        seed_nums.append(list(map(int, num_seed.split())))             
    
    new = []
    while seed_ranges:
        l, r = seed_ranges.pop()    
    
        for dest, source, length in seed_nums:
            max_range = source + length            
            
            if l >= source and r < max_range:
                new.append((l - source + dest, r - source + dest))
                break
            elif l >= source and r >= max_range and l < max_range:
                new.append((l - source + dest, max_range - source + dest))
                seed_ranges.append((max_range, r))
                break
            elif l < source and r < max_range and r > source:
                new.append((dest, r - source + dest))
                seed_ranges.append((l, source))
                break
            elif l < source and r > max_range:
                new.append((dest, max_range - source + dest))
                seed_ranges.append((l, source))
                seed_ranges.append((max_range, r))
                break
            
    new.append((l, r))
    seed_ranges = new

print("part 2:", sorted(seed_ranges)[0][0])
sum_1 = 0
sum_2 = 0
max_amount = {"red": 12, "green": 13, "blue": 14}

with open("inputs/input2.txt") as f:
    for line in f.readlines():
        game = line.strip().split(":")[0].split(" ")[-1]
        pulls = line.strip().split(":")[1].replace(";", ',').split(",")
        possible = True
        cube_count = {"red": 0, "green": 0, "blue": 0}
        
        for pull in pulls:
            num, color = pull.strip().split(" ")
            if int(num) > max_amount[color] and possible:
                possible = False
            if int(num) > cube_count[color]:
                cube_count[color] = int(num)
        
        if possible:
            sum_1 += int(game)
        
        cube = 1
        for value in cube_count.values():
            cube *= value
        sum_2 += cube
            
print("part 1:", sum_1)
print("part 2:", sum_2)
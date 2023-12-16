data = open("inputs/input15.txt").read().split(",")

total = 0

for d in data:
    string_score = 0
    for char in d:
        string_score += ord(char)
        string_score *= 17
        string_score %= 256
    
    total += string_score
    
print(total)
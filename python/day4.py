from collections import defaultdict

total_1 = 0
total_2 = 0
ticket_counter = defaultdict(int)
    
with open("inputs/input4.txt") as f: 
    for line in f.readlines():
        game, line = line.strip().split(":")
        game = int(game.split()[1])
        line = line.split("|")
        win_num, my_num = set(line[0].split()), set(line[1].split())
        
        ticket_score = len(win_num & my_num)
        ticket_counter[game] += 1
        
        if ticket_score > 0:
            score = 1
            for n in range(ticket_score - 1):
                score *= 2
            total_1 += score
            
            for n in range(1, ticket_score + 1):
                ticket_counter[game + n] += 1 * ticket_counter[game]

       
for n in ticket_counter.values():
    total_2 += n

print("part 1:", total_1)
print("part 2:", total_2)
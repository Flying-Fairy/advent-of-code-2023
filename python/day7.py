from collections import Counter, defaultdict

hands_list = []
hands_dict = defaultdict(list)
card_score = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}

with open("inputs/input7.txt") as f:
    for line in f.readlines():
        hand, bid = line.split()
        hand = " ".join(hand)
        
        for key, value in card_score.items():
            hand = hand.replace(key, value)
        
        hand = list(map(int, hand.split()))    
        hand_check = sorted(Counter(hand).values())
        hand_score = len(hand_check)
        
        if hand_score == 3 and hand_check[-1] == 2:
            hand_score = 3.1
        
        elif hand_score == 2 and hand_check[-1] == 3:
            hand_score = 2.1
        
        hands_dict[hand_score].append((hand, int(bid)))

hands_dict = dict(sorted(hands_dict.items(), reverse=True))
sorted_bid = []
total_1 = 0

for key, value in hands_dict.items():
    temp = sorted(value)
    for x in temp:
        sorted_bid.append(x[1])

for n, b in enumerate(sorted_bid):
    total_1 += b * (n + 1)

print("part 1:", total_1)
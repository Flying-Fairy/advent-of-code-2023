from collections import defaultdict

data = open("inputs/input15.txt").read().split(",")

boxes = defaultdict(list)
total = 0

def hash_label(label):
    label_score = 0
    
    for char in label:
        label_score += ord(char)
        label_score *= 17
        label_score %= 256
    
    return label_score

for d in data:
    if "=" in d:
        replace = False
        label, focal = d.split("=")
        label_num = hash_label(label)
        
        if boxes[label_num]:
            for i, b in enumerate(boxes[label_num]):
                if label == b.split()[0]:
                    replace = True
                    replace_index = i
                    break
                    
        if replace:
            boxes[label_num][replace_index] = label + " " + focal
        else:    
            boxes[label_num].append(label + " " + focal)

    if "-" in d:
        label = d[:-1]
        label_num = hash_label(label)
        
        if boxes[label_num]:
            for i, b in enumerate(boxes[label_num]):
                if label in b.split()[0]:
                    del boxes[label_num][i]

for key in boxes:
    if boxes[key]:
        for i, box in enumerate(boxes[key]):
            focal = int(box.split()[1])
            total += (key + 1) * (i + 1) * focal
            
print(total)
            
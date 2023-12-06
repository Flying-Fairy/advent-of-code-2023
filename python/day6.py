from math import prod

course = []
no_space = []
score_list = []

with open("inputs/input6.txt") as f:
    for line in f.readlines():
        course.append(list(map(int, line.split()[1:])))
        no_space.append(int("".join(line.split()[1:])))

for index, time in enumerate(course[0]):
    score = 0
    for n in range(1, time + 1):
        if (n * (time - n)) > course[1][index]:
            score += 1
    score_list.append(score)

print("part 1", prod(score_list))

score = 0
for n in range(1, no_space[0] + 1):
    if (n * (no_space[0] - n)) > no_space[1]:
        score += 1

print("part 2:", score)

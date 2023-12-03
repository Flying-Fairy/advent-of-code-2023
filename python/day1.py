sum = 0
valid_num = {'one': 'on1e', 'two': 'tw2o', 'three': 'thr3e', 'four': 'fo4ur',
             'five': 'fi5ve', 'six': 'si6x', 'seven': 'sev7en', 'eight': 'ei8ght',
             'nine': 'ni9ne'}

with open("inputs/input1.txt") as f:
    for line in f.readlines():
        digits = []
        for key, value in valid_num.items():
            line = line.replace(key, value)
        for c in line:
            if c.isdigit():
                digits.append(c)
            
        sum += int(digits[0] + digits[-1])

print(sum)
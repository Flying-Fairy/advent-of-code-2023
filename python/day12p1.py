total = 0

def count(target, nums):
    if not target:
        return 1 if not nums else 0 # If both are empty, target meets all nums requirements.
    if not nums:
        return 0 if "#" in target else 1 # target has "." or "?" and can be ignored.
    
    score = 0
    
    # for every "?", recursively check for both "." and "#".
    if target[0] in ".?":
        score += count(target[1:], nums)
    
    if target[0] in "#?":
        if nums[0] <= len(target) and "." not in target[:nums[0]]:
            if (nums[0] == len(target) or target[nums[0]] != "#"):
                score += count(target[nums[0] + 1:], nums[1:])

    return score

with open("inputs/test.txt") as f:
    for line in f.readlines():
        spring, nums = line.split()
        nums = list(map(int, nums.split(",")))
        
        total += count(spring, nums)

print(total)
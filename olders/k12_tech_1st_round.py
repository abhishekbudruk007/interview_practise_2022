# Input: \
candidates = [2, 3, 6, 7]
target = 7

# Output: [[2, 2, 3], [7]]


def candidate_comb(candidates, target):
    sum = 0
    output = []
    for i in range(1,len(candidates)+1):
        if candidates[i] == target:
            output.append(candidates[i])
        sum = candidates[i]*2
        if sum < target:
            sum = sum + candidates[i+1]
            if sum > target:
                continue
            output.append(candidates[i])
            output.append(candidates[i])
            output.append(candidates[i+1])
        if sum == target:
            return output

print(candidate_comb(candidates, target))
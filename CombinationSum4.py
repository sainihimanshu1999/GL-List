'''This is a basic dp problem, we are making combination array and checking with current elements how many combinations
we can make'''


def combinationSum(nums,target):
    nums.sort()
    combs = [1]+[0]*(target)

    for i in range(target+1):
        for num in nums:
            if num>i:
                break
            combs[i] += combs[i-num]

    return combs[target]
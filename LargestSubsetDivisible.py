'''Just do simple traversing for this question'''


def largestSubset(nums):

    nums.sort()

    result = [[num] for num in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j]== 0 and len(result[i])<len(result[j])+1:
                result[i] =  result[j] + [nums[i]]


    return max(result,key=len)


nums = [1,2,4,8 ]
print(largestSubset(nums))
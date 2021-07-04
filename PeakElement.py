'''It is an easy questionjust have to return any of the peak element'''


def peakElement(nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return i-1

    return len(nums)-1
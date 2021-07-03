'''we have to find the next largest permutation'''


def nextPermutation(nums):

    i=j=len(nums)-1

    while i>0 and nums[i-1]>=nums[i]:
        i-=1


    if i == 0:
        nums.sort()
        return nums

    k = i-1

    while nums[j]<=nums[k]:
        j-=1


    nums[j],nums[k] = nums[k],nums[j]

    left = k+1
    right = len(nums)-1


    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
    return nums


nums = [1,3,2]
print(nextPermutation(nums))
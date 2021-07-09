'''In wiggle sort it's basically nums[0]<nums[1]>nums[2]<nums[3]...and so on'''

def wiggleSort(arr):
    nums = sorted(arr)

    for i in range(1,len(nums),2):
        arr[i] = nums.pop()

    for i in range(0,len(nums),2):
        arr[i] = nums.pop()


    return arr



nums = [1,5,1,1,6,4]
print(wiggleSort(nums))
'''It was an easy question, just little bit intutive'''

def summaryRanges(nums):
    if not nums:
        return []

    result = []
    start,i = 0,0

    while i<len(nums)-1:
        if nums[i]+1 != nums[i+1]:
            result.append(solve(nums[start],nums[i]))
            start = i+1
        
        i+=1


    result.append(solve(nums[start],nums[i]))

    return result


def solve(l,r):
    if l==r:
        return str(l)

    else:
        return str(l)+'->'+str(r)

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
'''Smallest range which covers element covers k list, we do it by using heap'''

from heapq import *

def smallestRange(nums):

    heap = [(row[0],i,0) for i,row in enumerate(nums)]
    heapify(heap)

    ans = float('-inf'),float('inf')

    right = max(row[0] for row in nums)

    while heap:
        left,i,j = heappop(heap)

        if right-left<ans[1]-ans[0]:
            ans = left,right

        if j+1 == len(nums[i]):
            return ans
        
        val = nums[i][j+1]
        right = max(right,val)

        heappush(heap,(val,i,j+1))


nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(smallestRange(nums))


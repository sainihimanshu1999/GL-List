'''We use deque in this question, the answer is pretty neat'''

from collections import deque

def maxSlidingWindow(nums,k):
    q = deque()
    result = []


    for i,curr in enumerate(nums):
        while q and nums[q[-1]] <=curr:
            q.pop()

        q.append(i)

        if i == i-k:
            q.popleft()

        if i>=k-1:
            result.append(nums[q[0]])

    return result


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))
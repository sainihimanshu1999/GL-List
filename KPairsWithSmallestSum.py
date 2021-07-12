'''k pair with smallest sum'''

from heapq import *

def kpairssmallestsum(nums1,nums2,k):
    if not nums1 or not nums2:
        return 0
    result = []
    heap = [(nums1[0]+nums2[0],0,0)]
    visited = set((0,0))


    while len(result)<k and heap:
        sumi,x,y = heappop(heap)
        result.append([nums1[x],nums2[y]])

        if x+1<len(nums1) and (x+1,y) not in visited:
            heappush(heap,(nums1[x+1]+nums2[y],x+1,y))
            visited.add((x+1,y))

        if y+1<len(nums2) and (x,y+1) not in visited:
            heappush(heap,(nums1[x]+nums2[y+1],x,y+1))
            visited.add((x,y+1))

    return result


nums1 = [1,1,2]
nums2 = [1,2,3]
k = 3

print(kpairssmallestsum(nums1,nums2,k))


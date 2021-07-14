'''kth smallest element in sorted ascending matrix'''

from heapq import *

def kthSmallest(matrix,k):
    m,n = len(matrix),len(matrix[0])
    heap = []

    for r in range(m):
        for c in range(n):
            heappush(heap,-matrix[r][c])

            if len(heap)>k:
                heappop(heap)

    return -heappop(heap)

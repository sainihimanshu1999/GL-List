'''Just used BFS'''

from collections import deque

def maximumLevel(root):
    level,maxLevel = 0,0
    maxi = float('-inf')
    q = deque()
    q.append([root,level])

    while q:
        sumi = 0
        for i in range(len(q)):
            node,level = q.popleft()
            sumi += node.val
            if node.left: q.append([node.left,level+1])
            if node.right: q.append([node.right,level+1])
        
        if maxi<sumi:
            maxi,maxLevel = sumi,level
    
    return maxLevel

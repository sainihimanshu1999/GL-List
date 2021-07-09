'''minimum domino's rotations and we have to make all the elements in the top and bottom in the domino'''

def domino(tops,bottoms):
    if len(tops) != len(bottoms):
        return -1

    if len(tops)==0:
        return 0


    for cand in set(tops[0],bottoms[0]):
        topCount,bottomCount =0,0

        for i in range(len(tops)):
            if cand not in (tops[i],bottoms[i]):
                break
            topCount += int(cand != bottoms[i])
            bottomCount += int(cand != tops[i])

        else:
            return min(topCount,bottomCount)


    return -1

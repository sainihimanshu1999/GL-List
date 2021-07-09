'''when lists are divided into two parts and those parts contains equal number of distinct elements then than split
is called good split'''

from collections import Counter

def goodSplit(s):
    left = Counter()
    right = Counter(s)

    result = 0

    for c in s:
        left[c] +=1
        right[c] -=1

        if right[c] == 0:
            del right[c]
        
        if len(left) == len(right):
            result +=1

    return result


print(goodSplit('aacaba'))
'''This solution is pretty simple but it often gives TLE'''

from collections import defaultdict
def countRange(nums,lower,upper):

    prefixSum = [0]

    for num in nums:
        prefixSum.append(prefixSum[-1]+num)


    result = 0
    dic = defaultdict(int)

    for pref in prefixSum:
        for target in range(lower,upper+1):
            if pref-target in dic:
                result+= dic[pref-target]
        
        dic[pref] +=1
    
    return result
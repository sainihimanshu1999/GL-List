'''In this question we have to find the maximum length of subarray with at most two distinct elements'''

from collections import Counter

def fruitBasket(fruits):
    left,result =0,0
    count = Counter()


    for right in range(len(fruits)):
        count[fruits[right]]+=1

        while len(count)>2:
            
            count[fruits[left]]-=1

            if not count[fruits[left]]:
                count.pop(fruits[left])

            left +=1

        result = max(result,right-left+1)
    
    return result   

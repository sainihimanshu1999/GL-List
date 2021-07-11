'''This question is hard, but it's not baout what it shows it's more about the logic with which you will approach this'''

def patches(nums,n):
    result = 0
    covered = 0

    for num in nums:
        while num>covered+1:
            result +=1
            covered = covered*2+1

            if covered>=n:
                return result
        
        covered += num
        if covered>=n:
            return result

    while covered<n:
        result +=1
        covered = covered*2+1
    return result
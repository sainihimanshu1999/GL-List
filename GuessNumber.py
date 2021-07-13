'''Guessing number using api'''

def guess(n):
    low = 1
    high = n

    while low<=high:
        mid = (low+high)//2
        result = guess(mid)

        if result == 0:
            return mid

        elif result == -1:
            high = mid -1

        else:
            low = mid+1

        


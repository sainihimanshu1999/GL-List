'''In bit manipulation if n&(n-1) gives us 0 then the number n is power of two else not'''


def powerTwo(n):
    if n == 0:
        return False

    if n&(n-1):
        return False
    else:
        return True



print(powerTwo(1024))
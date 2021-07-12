'''This question is done by using permutation and combination'''


def uniqueDigits(n):
    if n == 0:
        return 1

    if n == 1:
        return 10

    choices = 9
    result = 0


    for i in range(1,n):
        choices = choices*(10-i)
        result += choices

    return result
'''letter combination in phone number using recursion and dictionary'''

def letterCombination(digits):
    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return list(dic[digits[0]])


    previous = letterCombination(digits[:-1])
    result = dic[digits[-1]]

    return [x+y for x in result for y in previous]
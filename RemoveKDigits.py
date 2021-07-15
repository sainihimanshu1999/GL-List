'''In this question we are going to use stack to rmove k digits from the number to make it smaller'''


def removeKdig(nums,k):
    stack = []

    for num in nums:
        while k>0 and stack and stack[-1]>num:
            k-=1
            stack.pop()

        stack.append(num)

    if k>0:
        stack = stack[:-k]

    return ''.join(stack).lstrip('0') or '0'
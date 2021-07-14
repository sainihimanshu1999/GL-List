'''In this question we just have to use stack'''

def decodeString(s):
    stack = []
    currStr = ''
    currNum = 0


    for i in s:

        if i == '[':
            stack.append(currStr)
            stack.append(currNum)
            currStr = ''
            currNum = 0

        elif i ==']':
            num = stack.pop()
            prevStr = stack.pop()
            currStr = prevStr+num*currStr

        elif i.isdigit():
            currNum = int(i) + 10*currNum
        else:
            currStr +=i
    return currStr


s = '2[ab4[c]]3[cd]ef'
print(decodeString(s))
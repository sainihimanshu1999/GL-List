'''Basic calculator is done using stack'''

def basicCalculator(s):
    result,num = 0,0
    sign,stack = 1,[]

    for digit in s:
        if digit.isdigit():
            num = num*10+int(digit)
            
        if digit in ['+','-']:
            result += sign*num
            num = 0
            sign = 1 if digit == '+' else -1
            
        elif digit == '(':
            stack.append(result)
            stack.append(sign)
            sign,result =1,0
            
        elif digit == ')':
            result += sign*num
            result *= stack.pop()
            result += stack.pop()
            num = 0

    return result+num*sign


s = "(1+(4+5+2)-3)+(6+8)"
print(basicCalculator(s))

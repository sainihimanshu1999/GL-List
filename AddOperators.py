'''Adding '+', '-','*', operand in the giver string operation so that our expression sum will lead to target
eval function in python does the same thing'''

def Operators(nums,target):
    n = len(nums)
    result = []


    def recurse(index,prev_operand,curr_operand,value,string):
        if index == n:
            if value == target and curr_operand == 0:
                result.append(''.join(string[1:]))
            return

        curr_operand = curr_operand*10+int(nums[index])
        operator_string = str(curr_operand)

        if curr_operand>0:
            recurse(index+1,prev_operand,curr_operand,value,string)

        string.append('+')
        string.append(operator_string)
        recurse(index+1,curr_operand,0,value+curr_operand,string)
        string.pop()
        string.pop()


        if string:
            string.append('-')
            string.append(operator_string)
            recurse(index+1,-curr_operand,0,value-curr_operand,string)
            string.pop()
            string.pop()


            string.append('*')
            string.append(operator_string)
            recurse(index+1,curr_operand*prev_operand,0,value-prev_operand+(curr_operand*prev_operand),string)
            string.pop()
            string.pop()


    recurse(0,0,0,0,[])
    return result

num = "123"; target = 6
print(Operators(num,target))
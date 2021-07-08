'''Removing dulplicate in the string'''

def duplicate(s):  
    last_occurence = {c:i for i,c in enumerate(s)}
    stack = ['!']
    visited = set()


    for i, char in enumerate(s):
        if char in visited:
            continue
        
        while(char<stack[-1] and last_occurence[stack[-1]]>i):
            visited.remove(stack.pop())

        visited.add(char)
        stack.append(char)

    return ''.join(stack[1:])


print(duplicate('bcabc'))
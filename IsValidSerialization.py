'''We have to check whether this preorder serialization of tree is valid or not'''

def validSerialization(preorder):

    pre = preorder.split(',')

    slots = 1

    for p in pre:
        if not slots:
            return False

        if p == '0':
            slots -=1

        else:
            slots +=1

    return slots == 0
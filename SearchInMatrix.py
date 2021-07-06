'''This is a simple question'''


def searchInMatrix(mat,target):
    x = 0
    y = len(mat[0])-1

    while x<len(mat) and y>=0:
        if target[x][y]>target:
            y-=1
        elif target[x][y]<target:
            x+=1

        else:
            return True

    return False
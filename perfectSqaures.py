'''We use basic ds to solve this question'''


def perfectSquares(n):

    if n<2:
        return n

    i = 1
    squares = []
    while i*i<=n:
        squares.append(i*i)
        i+=1

    count = 0
    num = {n}

    while num:
        count +=1 
        temp = set()

        for x in num:
            for y in squares:
                if x==y:
                    return count

                if x<y:
                    break

                temp.add(x-y)

        num = temp
    
    return count


print(perfectSquares(12))
                

'''In this question we just have to follow the basics, we will have set which till the end will record only
the most outside point of the rectangle and then we will calculate the area of that rectangle and check whether
this area is equal to the area of each rectangle which we have added before'''

def perfectRectangle(rectangles):
    valid = set()
    area = 0

    for x1,y1,x2,y2 in rectangles:
        top_l = (x1,y2)
        top_r = (x2,y2)
        bottom_l = (x1,y1)
        bottom_r = (x2,y1)

        area += (y2-y1)*(x2-x1)

        for i in [top_l,top_r,bottom_l,bottom_r]:
            if i not in valid:
                valid.add(i)
            else:
                valid.remove(i)

    if len(valid)!= 4:
        return False

    valid = sorted(valid)
    #print(valid,area)
    (x1,y1) = valid.pop(0)
    (x2,y2) = valid.pop()

    return area == (y2-y1)*(x2-x1)


rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(perfectRectangle(rectangles))
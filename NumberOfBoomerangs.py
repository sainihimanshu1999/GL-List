'''This question was pretty tricky, we just have to create a dictionary of points having the same distance form the certain point'''


def boomerangs(points):
    count = 0
    for i in range(len(points)):
        dic = {}
        for j in range(len(points)):
            dist = pow(points[i][0] - points[j][0]) + pow(points[i][1]-points[j][1])
            count += dic.get(dist,0)
            dic[dist] = dic.get(dist,0)+1


    return count*2
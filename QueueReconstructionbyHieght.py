'''In this question we have to sort the queue in reverse order and then add people accordin to thier postion'''


def queueReconstruct(people):
    result = []
    people = sorted(people, key=lambda x: (-x[0],x[1]))

    for p in people:
        result.insert(p[1],p)

    return result
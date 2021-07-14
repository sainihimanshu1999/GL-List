'''Length of absolute path in directory, we can maintain a dictionary and should minus the '\t' from the path'''

def absolutePath(input):
    result = 0
    dic = {}

    for s in input.splitlines():
        depth = s.count('\t')

        if '.' not in s:
            dic[depth] = len(s)-depth

        else:
            curr = len(s)+sum([dic[v] for v in range(depth)])

            result = max(curr,result)

    return result
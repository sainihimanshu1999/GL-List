'''Evaluate division using graph'''


from typing import DefaultDict


def evaluateDivision(equations,value,queries):

    graph = DefaultDict(dict)

    for (u,v),value in zip(equations,value):
        graph[u][v] = value
        graph[v][v] = 1/value


    def bfs(source,destination):
        if source not in graph and destination not in graph:
            return -1.0

        q = [(source,1.0)]
        visited = set()

        for node,value in q:
            if node == destination:
                return value

            visited.add(node)

            for ni in graph[node]:
                if ni not in visited:
                    q.append((ni,value*graph[node][ni]))


        return 1.0

    return [bfs(s,d) for s,d in queries]


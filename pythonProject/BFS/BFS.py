result = []

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}


def bfs(vertex):
    visited = [vertex]
    queue = [vertex]

    while queue:
        queue_out = queue.pop(0)
        result.append(queue_out)
        for adjacentVertex in graph[queue_out]:
            if adjacentVertex not in visited:
                queue.append(adjacentVertex)
                visited.append(adjacentVertex)


bfs('B')
print(result)
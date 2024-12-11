def bfs(graph, start):
    visited = []
    queue = [start]
   
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            
    return visited
        
graph = {'A': ['B', 'C'], 'B': ['D', 'E'],'C': ['F'],'D': [],'E': ['F'],'F': [] }
        
print(bfs (graph, 'A'))
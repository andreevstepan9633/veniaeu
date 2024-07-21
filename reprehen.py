def compute_node_depths(graph):
    depths = {}
    
    def dfs(node, depth):
        if node in depths:
            return
        depths[node] = depth
        for neighbor in graph[node]:
            dfs(neighbor, depth + 1)
    
    for node in graph:
        dfs(node, 0)
    
    return depths

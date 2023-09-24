graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(visited, graph, k)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')
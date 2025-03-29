#Graph representation
#Initialize variables
#Implement logic

from collections import deque  

def BFS (graph, node):
    #initialization
    visited = set()                             #track visited nodes
    visited.add(node)                            #add start node to visited
    queue = deque([node])                        #initialize the queue, starting at A
    result = []

    if node not in graph:
        return None

    #exploration
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def BFS2 (graph, node):
    #initialization
    visited = set()                             #track visited nodes
    # visited.add(node)                            #add start node to visited
    queue = deque([node])                        #initialize the queue, starting at A
    result = []

    if node not in graph:
        return None

    #exploration
    while queue:
        current = queue.popleft()
        if(current in visited):
            continue
        result.append(current)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                # visited.add(neighbor)
                queue.append(neighbor)

    return result   

def BFS_ignore_direction (graph, node):
    visited = set()                            
    result = []

    for node in graph:
        if node not in visited:
            queue = deque([node])
            visited.add(node)
            result.append(node)

        while queue:
            current = queue.popleft()
    
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    result.append(neighbor)
    return result

#directed graph 
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}      #representation using adjacency list
# graph = { 0: [2, 1, 3], 2: [4], 1: [], 3: [], 4: []}

#undirected graph
graph1 = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}











graph2 = {
    0: [1, 2], 
    1: [0, 3, 4], 
    2: [0, 5, 4], 
    3: [1], 
    4: [1, 5, 2], 
    5: [2, 4]
}


#call
print(BFS(graph2, 9))
print(BFS(graph2, 0))
print(BFS(graph2, 2))
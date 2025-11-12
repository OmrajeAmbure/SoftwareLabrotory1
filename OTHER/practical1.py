from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Main Program (Menu Driven)
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    """
    Sample Graph:       
        A
      /   \
     B     C
    / \     \
   D   E     F
        \   /
          ---
    """
    print("BFS traversal starting from vertex A:")
    bfs(graph, 'A')

    print("\nDFS traversal starting from vertex A:")
    dfs(graph, 'A')

    while True:
        choice = input("\n\nEnter 1 for BFS, 2 for DFS, or 'exit' to quit: ")

        if choice == '1':
            start_vertex = input("Enter the starting vertex for BFS: ")
            print("BFS traversal starting from vertex", start_vertex + ":")
            bfs(graph, start_vertex)

        elif choice == '2':
            start_vertex = input("Enter the starting vertex for DFS: ")
            print("DFS traversal starting from vertex", start_vertex + ":")
            dfs(graph, start_vertex, visited=None)

        elif choice.lower() == 'exit':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

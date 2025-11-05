from collections import deque

# Function to perform BFS Traversal
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS Traversal:", end=" ")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Function to perform DFS Traversal (Recursive)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Main Program
if __name__ == "__main__":
    graph = {}

    print("Enter number of vertices:")
    n = int(input())
    print("Enter vertex names:")
    vertices = [input().strip() for _ in range(n)]

    for v in vertices:
        graph[v] = []

    print("\nEnter number of edges:")
    e = int(input())
    print("Enter edges (u v) meaning an undirected connection:")
    for _ in range(e):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)

    print("\nGraph Representation (Adjacency List):")
    for key, value in graph.items():
        print(key, ":", value)

    while True:
        print("\nMenu:")
        print("1. BFS Traversal")
        print("2. DFS Traversal")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            start = input("Enter starting vertex: ")
            bfs(graph, start)

        elif choice == "2":
            start = input("Enter starting vertex: ")
            print("\nDFS Traversal:", end=" ")
            dfs(graph, start)
            print()

        elif choice == "3":
            break

        else:
            print("Invalid Choice! Try again.")

from collections import deque  # Import deque, which is a special kind of list optimized for fast appends and pops from both ends

# Define the simplified Romania city map as a graph (using a dictionary)
romania_map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Oradea'],
    'Oradea': ['Sibiu'],
    'Timisoara': ['Lugoj'],
    'Lugoj': ['Mehadia'],
    'Mehadia': ['Dobreta'],
    'Dobreta': ['Craiova'],
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Bucharest'],
    'Rimnicu Vilcea': ['Pitesti'],
    'Pitesti': ['Bucharest'],
    'Craiova': ['Pitesti'],
    'Bucharest': []  # Bucharest has no further connections (it's the goal)
}


# Function to perform Breadth-First Search and find the shortest path between two cities
def bfs_path(start, goal, graph):
    visited = set()  # Set to keep track of visited cities (to avoid visiting the same city again)
    queue = deque([[start]])  # Initialize the queue with a path that only contains the start city

    while queue:
        path = queue.popleft()  # Take the first path from the queue (FIFO)
        city = path[-1]  # Get the last city in the current path

        if city == goal:
            return path  # If this city is the goal, return the complete path as the result

        if city not in visited:
            # Loop through all neighboring cities connected to the current city
            for neighbor in graph.get(city, []):
                new_path = list(path)  # Copy the current path
                new_path.append(neighbor)  # Add the neighbor to the copied path
                queue.append(new_path)  # Add this new path back into the queue for future exploration

            visited.add(city)  # Mark the current city as visited

    return None  # If we go through the queue and never find the goal, return None


# Run the BFS algorithm to find the shortest path from Arad to Bucharest
shortest_path = bfs_path('Arad', 'Bucharest', romania_map)

# Display the result
if shortest_path:
    print("Shortest path from Arad to Bucharest (BFS):")
    # Before : shortest_path = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
    # After : shortest_path = ['Arad → Sibiu → Fagaras → Bucharest']
    # Join the list of city names with arrows to make it look nice (e.g., Arad → Sibiu → Fagaras → Bucharest)
    print(" → ".join(shortest_path))
else:
    print("No path found.")

from collections import deque
import time


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# ---------------- Graph ----------------
number_of_nodes = 500

graph = {}

for i in range(number_of_nodes):
    graph[i] = []

    if i + 1 < number_of_nodes:
        graph[i].append(i + 1)

    if i + 2 < number_of_nodes:
        graph[i].append(i + 2)

    if i + 3 < number_of_nodes:
        graph[i].append(i + 3)


start = 0
goal = number_of_nodes - 1


# ---------------- Timing ----------------
def measure_algorithm(algorithm, runs=10):

    times = []
    nodes = 0

    for _ in range(runs):

        start_time = time.perf_counter()

        nodes = algorithm(graph, start, goal)

        end_time = time.perf_counter()

        elapsed_time = (end_time - start_time) * 1000

        times.append(elapsed_time)

    best_time = min(times)
    average_time = sum(times) / len(times)
    worst_time = max(times)

    return best_time, average_time, worst_time, nodes


# ---------------- Results ----------------
bfs_best, bfs_average, bfs_worst, bfs_nodes = measure_algorithm(bfs)

dfs_best, dfs_average, dfs_worst, dfs_nodes = measure_algorithm(dfs)


print("\n========== BFS vs DFS PROFILING ==========")

print("\nBFS Results")
print("Nodes Expanded:", bfs_nodes)
print(f"Best Time:    {bfs_best:.6f} ms")
print(f"Average Time: {bfs_average:.6f} ms")
print(f"Worst Time:   {bfs_worst:.6f} ms")

print("\nDFS Results")
print("Nodes Expanded:", dfs_nodes)
print(f"Best Time:    {dfs_best:.6f} ms")
print(f"Average Time: {dfs_average:.6f} ms")
print(f"Worst Time:   {dfs_worst:.6f} ms")

print("\n========== COMPARISON ==========")
print(f"BFS Average Time: {bfs_average:.6f} ms")
print(f"DFS Average Time: {dfs_average:.6f} ms")
print(f"BFS Nodes Expanded: {bfs_nodes}")
print(f"DFS Nodes Expanded: {dfs_nodes}")
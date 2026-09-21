from collections import deque
import heapq
import time

# Goal state for 8-Puzzle
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Moves: Up, Down, Left, Right
MOVES = [-3, 3, -1, 1]


def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    row, col = zero_pos // 3, zero_pos % 3

    for move in MOVES:
        new_pos = zero_pos + move
        new_row, new_col = new_pos // 3, new_pos % 3

        if 0 <= new_pos < 9 and abs(row - new_row) + abs(col - new_col) == 1:
            state_list = list(state)
            state_list[zero_pos], state_list[new_pos] = (
                state_list[new_pos],
                state_list[zero_pos],
            )
            neighbors.append(tuple(state_list))
    return neighbors


def manhattan_distance(state):
    distance = 0
    for i, val in enumerate(state):
        if val != 0:
            target_row, target_col = (val - 1) // 3, (val - 1) % 3
            current_row, current_col = i // 3, i % 3
            distance += abs(target_row - current_row) + abs(
                target_col - current_col
            )
    return distance


# Algorithm A: Breadth-First Search (BFS)
def run_bfs(start_state):
    start_time = time.perf_counter()
    queue = deque([start_state])
    visited = {start_state}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL_STATE:
            break

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms, nodes_expanded


# Algorithm B: A* Search
def run_astar(start_state):
    start_time = time.perf_counter()
    open_set = [(manhattan_distance(start_state), 0, start_state)]
    g_scores = {start_state: 0}
    visited = set()
    nodes_expanded = 0

    while open_set:
        _, g, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == GOAL_STATE:
            break

        for neighbor in get_neighbors(current):
            tentative_g = g + 1
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms, nodes_expanded


if __name__ == "__main__":
    start_puzzle = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    # Run BFS 3 times
    bfs_times, bfs_nodes = [], []
    for _ in range(3):
        t, n = run_bfs(start_puzzle)
        bfs_times.append(t)
        bfs_nodes.append(n)

    # Run A* 3 times
    astar_times, astar_nodes = [], []
    for _ in range(3):
        t, n = run_astar(start_puzzle)
        astar_times.append(t)
        astar_nodes.append(n)

    # Calculate Best (min), Worst (max), and Average (sum/3)
    best_bfs = min(bfs_times)
    worst_bfs = max(bfs_times)
    avg_bfs = sum(bfs_times) / 3

    best_astar = min(astar_times)
    worst_astar = max(astar_times)
    avg_astar = sum(astar_times) / 3

    # Output results
    print("\n" + "=" * 55)
    print("           SLE-2 PROFILING RESULTS (3 RUNS)           ")
    print("=" * 55)
    print(f"{'Metric':<20} | {'BFS (Algorithm A)':<15} | {'A* (Algorithm B)':<15}")
    print("-" * 55)
    print(f"{'Best Time (ms)':<20} | {best_bfs:<15.4f} | {best_astar:<15.4f}")
    print(f"{'Worst Time (ms)':<20} | {worst_bfs:<15.4f} | {worst_astar:<15.4f}")
    print(f"{'Average Time (ms)':<20} | {avg_bfs:<15.4f} | {avg_astar:<15.4f}")
    print(f"{'Nodes Expanded':<20} | {bfs_nodes[0]:<15} | {astar_nodes[0]:<15}")
    print("=" * 55 + "\n")

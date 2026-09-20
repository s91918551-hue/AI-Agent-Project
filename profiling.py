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

    # Profiling BFS
    bfs_times, bfs_nodes = [], []
    for _ in range(3):
        t, n = run_bfs(start_puzzle)
        bfs_times.append(t)
        bfs_nodes.append(n)

    # Profiling A*
    astar_times, astar_nodes = [], []
    for _ in range(3):
        t, n = run_astar(start_parser := start_puzzle)
        astar_times.append(t)
        astar_nodes.append(n)

    avg_bfs_time = sum(bfs_times) / 3
    avg_astar_time = sum(astar_times) / 3

    print("\n" + "=" * 50)
    print("           SLE-2 PROFILING RESULTS            ")
    print("=" * 50)
    print(
        f"{'Metric':<20} | {'BFS (Algorithm A)':<15} | {'A* (Algorithm B)':<15}"
    )
    print("-" * 55)
    print(
        f"{'Avg Time (ms)':<20} | {avg_bfs_time:<15.4f} | {avg_astar_time:<15.4f}"
    )
    print(
        f"{'Nodes Expanded':<20} | {bfs_nodes[0]:<15} | {astar_nodes[0]:<15}"
    )
    print("=" * 50 + "\n")
SLE-2: Empirical Performance Analysis of BFS and DFS

1. Aim

To compare the empirical performance of Breadth First Search (BFS) and Depth First Search (DFS) using execution time, nodes expanded, and profiling data.

2. Problem Statement

BFS and DFS are fundamental search algorithms used for exploring graphs and state spaces. In this experiment, both algorithms are applied to the same graph and their performance is measured experimentally.

3. Algorithms Used

Breadth First Search (BFS)

BFS explores nodes level by level using a queue. It is useful when the shortest path in terms of number of edges is required.

Depth First Search (DFS)

DFS explores one branch deeply before backtracking. It uses a stack and can be useful for exploring large search spaces.

4. Experimental Setup

- Programming Language: Python
- Graph size: 1000 nodes
- Starting node: 0
- Goal node: 999
- Number of timing runs: 10
- Time measurement: "time.perf_counter()"
- Profiling tool: cProfile with SnakeViz
- Performance metrics:
  - Best execution time
  - Average execution time
  - Worst execution time
  - Nodes expanded

5. Performance Results

Algorithm| Best Time (ms)| Average Time (ms)| Worst Time (ms)| Nodes Expanded
BFS| 0.258400| 0.284590| 0.413000| 500
DFS| 0.239900| 0.334810| 0.666300| 500

All measured execution times are greater than 0.1 ms, making the differences measurable.

6. Profiling Results

The program was also analyzed using Python's cProfile and visualized using SnakeViz.

Important profiling observations:

- "measure_algorithm" had a cumulative time of approximately 0.05741 seconds.
- BFS was called 10 times with cumulative time of approximately 0.03613 seconds.
- DFS was called 10 times with cumulative time of approximately 0.02107 seconds.
- The total program execution recorded by cProfile was approximately 0.06122 seconds.
- Queue and stack operations such as "append", "popleft", "pop", and set operations were also recorded by the profiler.

7. Comparison

From the timing experiment, BFS had an average execution time of 0.284590 ms, while DFS had an average execution time of 0.334810 ms.

Both algorithms expanded 500 nodes for the selected graph and goal.

The best measured time was 0.239900 ms for DFS, while the worst measured time was 0.666300 ms for DFS. These values show that execution time can vary between individual runs because of normal system and Python runtime overhead.

The profiling results provide additional information about which functions and operations consume execution time.

8. AI Contribution

BFS and DFS are basic search techniques that are important in Artificial Intelligence. They can be used for state-space search, path finding, problem solving, and exploring possible solutions.

Empirical profiling helps an AI developer understand the practical computational cost of search algorithms and select an appropriate method for a particular problem.

9. Conclusion

The experiment successfully compared BFS and DFS using actual execution measurements. Best, average, and worst execution times were calculated over multiple runs, and the number of expanded nodes was recorded.

cProfile and SnakeViz were used to inspect the internal execution behavior of the program. The experiment demonstrates that theoretical complexity and practical execution performance can be studied together when evaluating AI search algorithms.
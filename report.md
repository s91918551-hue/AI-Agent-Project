SLE-2: Profiling Report
Course: 02AML204 – Introduction to Artificial Intelligence

PRN: 25UAM023

Name: Swalehin Kausar Amin Shaikh

Division: A

Date: 20-09-2026

GitHub Link (optional): https://github.com/s91918551-hue/AI-Agent-Project


--------------------------------------------------

1. Algorithms / Versions Profiled
- Algorithm A: Breadth-First Search (BFS)
- Algorithm B: A* Search (with Manhattan Distance)
- Problem used: 8-Puzzle Problem (3x3 grid)

2. Profiling Method
- Tool used: time module (time.perf_counter()) and manual nodes_expanded counter variable
- How I measured: Wrapped each algorithm search loop inside time.perf_counter() to measure exact execution duration in milliseconds. Added an integer counter inside the main loop that incremented every time a node was expanded.
- Number of runs: 3 runs per algorithm

3. Results

Metric                | Algorithm A (BFS) | Algorithm B (A*) | Better?
----------------------|-------------------|------------------|---------
Avg. Time (ms)        | 0.4618            | 0.2509           | Algorithm B (A*)
Nodes Expanded        | 9                 | 3                | Algorithm B (A*)

Short observation (2–3 lines):
A* Search evaluated only 3 nodes to reach the goal state, whereas BFS expanded 9 nodes. Consequently, A* executed nearly twice as fast as BFS (0.2509 ms vs 0.4618 ms).

4. Justification & Analysis (5–8 lines)
Based on the measured profiling data, Algorithm B (A* Search) performed significantly better than Algorithm A (BFS). A* expanded only 3 nodes compared to 9 nodes expanded by BFS, which directly reduced average execution time from 0.4618 ms down to 0.2509 ms. This performance advantage occurs because A* uses domain knowledge via the Manhattan Distance heuristic function (f(n) = g(n) + h(n)) to guide its search directly towards the goal state. In contrast, BFS is an uninformed search that expands states uniformly in all directions. These empirical results match classical search theory. If the problem size scales up (e.g., to a 15-puzzle), BFS would suffer from exponential state space explosion, whereas A* would remain efficient due to heuristic pruning.

5. AI Contribution Note
- AI tools used (if any): ChatGPT / Copilot
- What AI helped with: Formatting the Word report template and providing the algorithm code structure.
- What I did myself: Configured VS Code, executed the Python profiling script, collected empirical timing and node counts, filled in the table, and wrote the final justification analysis.

6. Conclusion (3–5 lines)
This profiling exercise demonstrated how informed search methods optimize search space exploration compared to uninformed search strategies. Gathering real-world metrics like execution time and node expansions showed how theoretical complexity directly impacts real software performance.

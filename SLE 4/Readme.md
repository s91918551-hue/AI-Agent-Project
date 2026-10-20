# SLE-4: Final Viva & Architecture Decision Record (ADR)

## 8-Puzzle Solver Using A* Search and Manhattan Distance

### 1. Student Information

- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **PRN:** 25UAM023
- **Name:** Swalehin Kausar Amin Shaikh
- **Division:** A
- **Date:** October 11, 2026
- **GitHub Repository:** https://github.com/s91918551-hue/AI-Agent-Project

---

### 2. Project Overview

The 8-Puzzle Solver is an AI-based application that finds a solution to the 8-puzzle problem using search algorithms. The puzzle consists of eight numbered tiles and one empty space arranged in a 3 × 3 grid.

The main objective is to move the tiles from an initial state to the goal state using the minimum number of moves.

This project uses **A* Search with the Manhattan Distance heuristic** to find an optimal solution efficiently.

### 3. Objectives

- To implement an AI search algorithm for solving the 8-puzzle problem.
- To understand the working of A* Search and BFS.
- To compare search algorithms using execution time and node expansions.
- To design the system using C4 architecture diagrams.
- To document the algorithm selection using an Architecture Decision Record (ADR).

### 4. Technologies Used

- **Programming Language:** Python
- **Search Algorithm:** A* Search
- **Heuristic Function:** Manhattan Distance
- **Priority Queue:** Python `heapq` module
- **Profiling:** Python `time` module and custom node counters
- **Architecture Modeling:** C4 diagrams
- **Version Control:** Git and GitHub

---

### 5. Architecture Decision Record (ADR)

**Title:** Selection of A* Search with Manhattan Distance over Breadth-First Search (BFS)

**Status:** Accepted

#### Context

BFS explores puzzle states level by level and can consume considerable time and memory as the search space increases. An efficient algorithm was required to find the shortest solution path while reducing unnecessary node expansions.

#### Decision

A* Search with the Manhattan Distance heuristic was selected as the primary search algorithm instead of BFS.

#### Alternatives Considered

1. **Breadth-First Search (BFS):** Explores states level by level and guarantees the shortest path when all moves have equal cost.
2. **A* with Misplaced Tiles:** Uses the number of misplaced tiles as its heuristic.
3. **Depth-First Search (DFS):** Explores deeper paths first but does not generally guarantee the shortest solution.

#### Rationale

A* evaluates states using the following formula:

`f(n) = g(n) + h(n)`

Where:
- `g(n)` is the cost of reaching the current state.
- `h(n)` is the estimated cost of reaching the goal.
- `f(n)` is the estimated total solution cost through that state.

Manhattan Distance calculates the total horizontal and vertical distance of each tile from its goal position, excluding the empty space.

It provides an admissible and consistent heuristic for the standard 8-puzzle. Therefore, A* can find an optimal solution when implemented correctly.

#### Consequences

**Advantages:**
- Finds a shortest solution path.
- Often expands fewer nodes than BFS.
- Uses heuristic information to guide the search.
- Can improve execution time on suitable puzzle configurations.

**Trade-offs:**
- Calculates a heuristic for evaluated states.
- Uses a priority queue with insertion and removal overhead.
- Can still consume significant memory for difficult puzzles.

---

### 6. SLE Journey Summary

#### SLE-1: Project Development

- Developed the initial 8-puzzle solver code in Python.
- Created the project structure.
- Set up Git version control and the GitHub repository.

#### SLE-2: Performance Evaluation

- Created `profiling.py` to measure execution time and node expansions.
- Compared BFS and A* Search.
- Documented the observations in `report.md`.

#### SLE-3: System Architecture

- Designed C4 architecture diagrams.
- Modeled the system at Context, Container, Component, and Code levels.
- Identified the responsibilities of input handling, search logic, heuristic evaluation, and output formatting.

#### SLE-4: Final Viva and ADR

- Documented the selection of A* Search with Manhattan Distance.
- Compared alternative algorithms.
- Explained the advantages and trade-offs of the selected approach.
- Prepared technical explanations for the final viva.

---

### 7. System Workflow

1. The user provides the initial puzzle state.
2. The input module validates the puzzle input.
3. The search engine initializes A* Search.
4. The heuristic evaluator calculates Manhattan Distance.
5. The priority queue selects the next state with the lowest estimated total cost.
6. The search continues until the goal state is reached or no solution is available.
7. The output module displays the solution path and relevant performance information.

---

### 8. AI Contribution Note

**AI Tool Used:** Gemini AI Assistant

**AI Assistance:**
- Helped structure the ADR.
- Improved the clarity of technical explanations.
- Assisted with trade-off descriptions and viva preparation.

**My Contribution:**
- Developed the original project code.
- Ran the profiling scripts.
- Recorded and reviewed performance metrics.
- Designed the C4 architecture diagrams.
- Reviewed the algorithm selection and technical trade-offs.

---

### 9. Viva Questions and Answers

**Q1. Why did you select A* instead of BFS?**

A* uses a heuristic to guide the search toward the goal and can reduce unnecessary node expansions. BFS explores states level by level without heuristic guidance.

**Q2. What is Manhattan Distance?**

It is the sum of the horizontal and vertical distances of each numbered tile from its goal position.

**Q3. Why is Manhattan Distance better than Misplaced Tiles?**

Manhattan Distance considers how far each tile is from its correct position, whereas Misplaced Tiles only counts tiles that are in the wrong position.

**Q4. What is a heuristic function?**

A heuristic function estimates the remaining cost from the current state to the goal state.

**Q5. What is the role of `heapq`?**

The Python `heapq` module provides a priority queue that helps A* select a state with the lowest priority value efficiently.

**Q6. Does A* guarantee an optimal solution?**

Yes, for the 8-puzzle, A* with an admissible Manhattan Distance heuristic finds an optimal solution when implemented correctly.

**Q7. What are the limitations of A*?**

A* can require substantial memory and computation for difficult puzzle states.

**Q8. What is an ADR?**

An Architecture Decision Record documents an important technical decision, the alternatives considered, the reasons for the decision, and its consequences.

---

### 10. Conclusion

The 8-Puzzle Solver demonstrates the application of artificial intelligence search techniques to a state-space problem. A* Search with Manhattan Distance was selected because it uses heuristic guidance and can reduce node expansions while preserving solution optimality. The SLE-1 to SLE-4 activities cover implementation, performance evaluation, architecture design, and technical decision documentation.

### 11. Project Repository

GitHub: https://github.com/s91918551-hue/AI-Agent-Project

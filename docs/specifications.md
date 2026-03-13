# Pathfinding Algorithms Project / Specification

## Overview
This project focuses on generating randomized 2D grid-based maps and evaluating the performance of pathfinding algorithms in dynamic environments. Users can experiment with different map sizes and algorithm choices, and visualize the results using a simple interface.


## Technologies Used

**Programming Languages**  
- **Python** – Implements pathfinding algorithms and map generation.  
- **Pygame** – Provides the frontend interface for map visualization.

**Supported Languages (Peer Reviews)**  
- Python


## Pathfinding Algorithms

**A\***  
- General-purpose algorithm for finding the shortest path in a weighted graph.

**LPA\*** (Lifelong Planning A\*)  
- Incremental pathfinding algorithm based on A\*, optimized for dynamic or changing environments.


## Problem Statement
- Generate dynamic, randomized 2D grid maps with a defined start and goal.  
- Compare and evaluate the efficiency and performance of A\* and LPA\* on these maps.


## Input & Usage

**Input:**  
- Specify map dimensions using x, y parameters.

**Usage:**  
1. Select the type of map to generate.  
2. Choose one or more pathfinding algorithms for evaluation.  
3. View the calculated path and algorithm performance statistics.


## Performance

Let:  
- **N** = total number of nodes  
- **b** = branching factor  
- **d** = depth of shortest path  
- **k** = nodes affected by a map change

**Space Complexity**  
- A\*: O(N)  
- LPA\*: O(N)

**Time Complexity**  
- **A\*** – Initial: O(b^d), Updates: O(b^d)  
- **LPA\*** – Initial: O(b^d), Updates: O(k log k)


## References
- [GeeksforGeeks – A* Algorithm](https://www.geeksforgeeks.org/dsa/a-search-algorithm/)  
- [Wikipedia – Lifelong Planning A*](https://en.wikipedia.org/wiki/Lifelong_Planning_A*)  
- [CMU Research – Lifelong Planning A*](https://www.ri.cmu.edu/publications/lifelong-planning-a/)

## Misc
- I am enrolled in the Bachelor’s in Computer Science program at the University of Helsinki.
- This specification and all documentation for the project will be written in English.

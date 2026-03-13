# Pathfinding Algorithms Project / Specification

## Overview
This project focuses on generating randomized 2D grid-based maps and evaluating the performance of pathfinding algorithms in static environments. Users can experiment with different map sizes and algorithm choices, and visualize the results using a simple interface. The main goal is to compare JPS and Fringe Search in terms of efficiency and speed on static 2D grids.

## Technologies Used

**Programming Languages**  
- **Python 3.13** – Implements pathfinding algorithms and map generation. 
- **pygame** – Provides the frontend interface for map visualization.

Notice: pygame does not currently support Python >3.14 https://github.com/pygame/pygame/issues/4627

**Supported Languages (Peer Reviews)**  
- Python

## Pathfinding Algorithms

**Jump Point Search (JPS)**
- Optimized A* for uniform-cost grids that skips intermediate nodes by evaluating only jump points. 

**Fringe Search**
- A* variant that manages the open list as a fringe queue.

## Problem Statement
- Generate static, randomized 2D grid maps with a defined start and goal.  
- Compare and evaluate the efficiency and performance of JPS and Fringe Search algorithms on these maps.

## Input & Usage

**Input:**  
- Specify map dimensions using x, y parameters.

**Usage:**  
1. Select the type of map to generate.  
2. Choose either JPS or Fringe Search for evaluation.  
3. View the calculated path and algorithm performance statistics.

## Performance

- N = total number of nodes  
- b = branching factor  
- d = depth of shortest path  

**Space Complexity**  
- JPS: O(N)  
- Fringe Search: O(N)

**Time Complexity**  
- JPS: Best-case: O(b^d)
- Fringe Search: Best-case: O(b^d)

## References
- JPS: https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/
- Fringe Search: https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf

## Misc
- I am enrolled in the Bachelor’s in Computer Science program at the University of Helsinki.  
- This specification and all documentation for the project will be written in English.

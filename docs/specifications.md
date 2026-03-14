# Pathfinding Algorithms Project / Specification

## Overview
This project focuses evaluating the performance of A* vs JPS pathfinding algorithms in Warcraft 3 maps. Users can select a starting point and goal on the map and compare JPS and A* algorithm performance on these maps. 

The WC3 maps 512x512 size by default and they are provided by [movingai.com](https://movingai.com/benchmarks/wc3maps512/index.html).

Map Format:
```type octile
height y
width x
map
where y and x are the respective height and width of the map.
The map data is store as an ASCII grid. The upper-left corner of the map is (0,0). The following characters are possible:

- passable terrain
G - passable terrain
@ - out of bounds
O - out of bounds
T - trees (unpassable)
S - swamp (passable from regular terrain)
W - water (traversable, but not passable from terrain)
```

## Technologies Used

- **Python 3.13** – Implements pathfinding algorithms and map generation. 
- **pygame** – Provides the frontend interface for map visualization.

Notice: pygame does not currently support Python >3.14 https://github.com/pygame/pygame/issues/4627

**Supported Languages (Peer Reviews)**  
- Python

## Pathfinding Algorithms

**A\***  
- General-purpose algorithm for finding the shortest path in a weighted graph.

**Jump Point Search (JPS)**
- Optimized A* for uniform-cost grids that skips intermediate nodes by evaluating only jump points.

## Problem Statement
- Evaluate and compare **A\*** and **Jump Point Search (JPS)** on Warcraft 3 maps.  
- Analyze how JPS pruning affects practical performance compared to A*.
- Visualize paths and measure performance.

## Input & Usage

- Users can select a map from the dropdown menu.
- Users can select a starting point and goal by clicking on the map.
- The app provides visuals for the pathfinding algorithms and displays statistics about their performance.

## Performance

- N = total number of nodes  
- b = branching factor  
- d = depth of shortest path  

**Space Complexity**  
- JPS: O(N)  
- A*: O(N)

**Time Complexity**  
- JPS: Worst-case: O(b^d)
- A*: Worst-case: O(b^d)


## References
- JPS: https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/
- A*: https://en.wikipedia.org/wiki/A*_search_algorithm
- Warcraft 3 Maps: https://movingai.com/benchmarks/wc3maps512/index.html

## Misc
- I am enrolled in the Bachelor’s in Computer Science program at the University of Helsinki.  
- This specification and all documentation for the project will be written in English.

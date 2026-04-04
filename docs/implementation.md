# Implementation

## Software Structure
The application is built in Python and using pygame library for visualization. Pygame was chosen for the UI because the implementation of the UI is was deemed simple enough for this project. However, since pygame does not currently support [Python >3.14](https://github.com/pygame/pygame/issues/4627) the drawback is that user must have older version of Python installed. 

The app uses A* and JPS pathfinding algorithms to perform comparison analysis in Warcraft 3 maps. In the current version of the software the pathfinding algorithms perform quite well under the self-builded benchmarker and the results are what are generally expected of the their usual performance.

## Pathfinding Algorithms

A* [source code](../src/astar.py)<br>
<br>
A* is most commonly used pathfinding algorithm in video games. A* checks all immediate neighbours at each step and it uses goal-aware heuristic to improve [Djikstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). The performance of A* is usually better than Djikstra thanks to the heuristic calculation, but in small maps it can have almost same performance as Djikstra.

JPS [source code](../src/jps.py)<br
<br>
JPS is an optimized A* for uniform grids. It scans certain directions and jumps to key selected key nodes. Nodes expansions are heavier than in A*, but total expandes nodes are often much lower than A* due to the optimization. In open maps the performance the performance of JPS is signifcant over A*, but in object dense maps that require lots of zigzag movement its advantage over A* will decrease due to the nature of the implementation.

The performance optimization will be more clear to the peer-reviewer when expanded nodes are visualized in the UI.

## Further Improvements
Note (04.04.2026): Test coverage still needs improvement. UI is currently missing two key features that are to be added later date: expanded nodes visualization and algorithm performance (only reported in terminal now). Pylint has been used since start of the project, but some of the issues have not been fixed yet. 

## Sources
- JPS: https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/
- JPS: https://harablog.wordpress.com/2011/09/07/jump-point-search/
- JPS: https://www.youtube.com/watch?v=afoQvbXvaiQ
- A*: https://en.wikipedia.org/wiki/A*_search_algorithm
- A* & Pygame related: https://www.youtube.com/watch?v=JtiK0DOeI4A
- Warcraft 3 Maps: https://movingai.com/benchmarks/wc3maps512/index.html

## AI Usage
- LLM (ChatGPT) was consulted regarding possible JPS performance issues, because "working" JPS pruning had a significantly higher runtime than A*. 
- LLM (ChatGPT) helped to recognize problem in JPS pruning rules compared to traditional JPS implementation. 
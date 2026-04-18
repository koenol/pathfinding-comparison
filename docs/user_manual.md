# User Manual

This is a work in progress, not much to see here yet. 

1. Choose a map from the dropdown menu
2. Select start (x,y) and goal (x,y) positions
3. Choose which pathfinding algorithm to run (A* vs JPS)
4. Expanded nodes, scanned nodes and shortest path found by the algorithm will be visualized in the user interface.
5. Runtime, expanded nodes, scanned nodes and path length are displayed in the user interface.

# Helpful Commands / Testing, coverage, etc.

Run tests
```
poetry run invoke test
```
Run benchmarker using default parameters
```
poetry run invoke perf-test
```
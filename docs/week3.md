- Finished A* pathfinder - seems to working as intended. Update: Changed A* to use heapq instead of PriorityQueue. This should decrease overhead, but it shouldn't affect performance that much. The main reason was to make comparison JPS more relevant. 
- JPS pathfinder pruning was harder than expected. I run into numerous issues:
    - Had to implement runtime, path length, nodes expanded comparison func early for terminal only due to numerous issues, e.g. Path/Jump was not always found. ~~PriorityQueue caused significant overhead compared to heapq and runtime became larger than A* even thou less nodes was expanded. Earlier version pruning with PQ runtime was still faster with less nodes expanded, but path was still longer than A* sometimes. I first thought that might be due to 4-way movement pruning when JPS is actually intended for 8-way movement,~but in the end jump rules and data structure type the main problem.~~  Update: Wrong, it's unlikely that the data structure had much to do with anything.
- Added automated benchmarking tool for pathfinder comparison. This is intended for performing large amount of benchmarks only, no UI vizualisation. Update:  Larger queries 1000+ take a long time, so it is recommend to keep -n 1000 for benchmarking. Considering adding a multiprocessing option, but unit tests take the priority now when it comes to testing.
- Next week the plan is to increase the amount of unit tests and coverage and improve github documentation for peer-review. Improving visualization of pathfinders traversed paths and reporting results in UI are also in the planning. Latter takes the priority for peer-review, but if possible both should be done next week.

Final Update: Found a mistake in JPS algorithm that was causing performance issues, spend 4-5 debugging and rebuilding on top of what I had already done earlier, saturday evening got ruined completely, and this was after I already said JPS was harder than I expected. Re-run the performance tests and re-commited yesterday and todays changes, should use rebase instead.

The summary etc can be found in test documentation, but I wanna talk about the summary a bit.<br>
[Test Documentation](test_report.md)<br>
Summary:<br>
Runtime faster: A*: 1342, JPS: 8658, Equal: 0<br>
Expanded fewer nodes: A*: 0, JPS: 9999, Equal: 1<br>
Shorter path length: A*: 3919, JPS: 0, Equal: 6081<br>

There is probably lots of edge cases where A* still performs better for a reason, e,g. very short paths, no valid path, I need to expand benchmark testing to get better understanding. At the moment I'm mainly worried about A* having shorter path length 40% of time even when JPS is expands less nodes majority of time. 

Hours Spent: 18h (Cumulative: 35h)
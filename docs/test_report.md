# Test Documentation

## W6 Coverage

```
poetry run pytest tests -q
poetry run coverage run -m pytest tests
poetry run coverage report
poetry run coverage html
```

![](/static/coverage6.png)

## Benchmark

Benchmark tool for pathfinder comparison is automated tool that lets user compare pathfinder performance using large amount of queries. The tool is designed for CLI only.

```
poetry run python -m tests.pathfinder_benchmark -n 10000 -r off
```
<b>Summary:</b><br>
Runtime faster: A*: 2330, JPS: 7670, Equal: 0<br>
Expanded fewer nodes: A*: 0, JPS: 9999, Equal: 1<br>
Scanned fewer nodes: A*: 9996, JPS: 4, Equal: 0<br>
Shorter path length: A*: 0, JPS: 0, Equal: 10000<br>
Average runtime: A*: 116ms, JPS: 35ms<br>

## Pylint

```
************* Module src.astar
src\astar.py:36:1: R0914: Too many local variables (16/15) (too-many-locals)
************* Module src.jps
src\jps.py:20:1: R0912: Too many branches (16/12) (too-many-branches)
src\jps.py:85:1: R0911: Too many return statements (9/6) (too-many-return-statements)
src\jps.py:161:1: R0914: Too many local variables (19/15) (too-many-locals)
************* Module src.map_handler
src\map_handler.py:5:0: R0902: Too many instance attributes (10/7) (too-many-instance-attributes)
************* Module src.ui
src\ui.py:10:0: R0902: Too many instance attributes (22/7) (too-many-instance-attributes)
src\ui.py:102:1: R0911: Too many return statements (9/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 9.87/10 (previous run: 9.87/10, +0.00)
```
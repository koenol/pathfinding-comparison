# Test Documentation

## W3 Coverage

Unit tests need more attention next week.

```
poetry run pytest tests -q
poetry run coverage run -m pytest tests
poetry run coverage report
poetry run coverage html
```

![](/static/coverage2.png)

## Benchmark

Benchmark tool for pathfinder comparison is automated tool that lets user compare pathfinder performance using large amount of queries. The tool is designed for CLI only.

```
poetry run python -m tests.pathfinder_benchmark -n 10000 -r off
```
<b>Summary:</b><br>
Runtime faster: A*: 1342, JPS: 8658, Equal: 0<br>
Expanded fewer nodes: A*: 0, JPS: 9999, Equal: 1<br>
Shorter path length: A*: 3919, JPS: 0, Equal: 6081<br>

## Pylint

Most of the issues are very minor. 
```
pylint src
```
Your code has been rated at 9.04/10 (previous run: 9.08/10, -0.04)
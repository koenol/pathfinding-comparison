# Test Documentation

## W4 Coverage

Unit tests need more attention next week.

```
poetry run pytest tests -q
poetry run coverage run -m pytest tests
poetry run coverage report
poetry run coverage html
```

![](/static/coverage3.png)

## Benchmark

Benchmark tool for pathfinder comparison is automated tool that lets user compare pathfinder performance using large amount of queries. The tool is designed for CLI only.

```
poetry run python -m tests.pathfinder_benchmark -n 10000 -r off (no exclusion criteria used)
```
<b>Summary:</b><br>
Runtime faster: A*: 2555, JPS: 7445, Equal: 0<br>
Expanded fewer nodes: A*: 0, JPS: 10000, Equal: 0<br>
Shorter path length: A*: 0, JPS: 0, Equal: 10000<br>
Average runtime: A*: 107ms, JPS: 47ms<br>

## Pylint

Most of the issues are very minor. 
```
pylint src
```
Your code has been rated at 9.04/10 (previous run: 9.08/10, -0.04)
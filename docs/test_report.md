# Test Documentation

Not much to see here yet, just W2 coverage.

```
poetry run pytest tests
poetry run coverage run -m pytest tests
poetry run coverage report
```

Name                   Stmts   Miss  Cover
------------------------------------------
src\app.py                32     32     0%
src\astar.py              37     37     0%
src\map_generator.py      45      9    80%
src\map_handler.py        28     20    29%
src\ui.py                102     88    14%
------------------------------------------
TOTAL                    244    186    24%
# Week 2 Progress Report

- Added pytest-dev to poetry and some basic tests. If I understood correctly the goal of the course is to test mainly that the algorithms behave correctly meaning there is not much to test for now. I might still add some few basics tests that checks all the files are correctly loaded.
- MapGenerator now loads all maps at once.
- Added UI class and dropdown menu for map switching.
- Added map (x,y) selection.
- Added map_handler class that handles map color updates, for now only updates start and end coordinates.
- Moved map-related coordinate handling from ui class to map_handler, map_generation still handles initial load.
- Studied A* a little bit and implemented some required methods for A* to start with. Plan is to complete A* pathfinder and visualization next week.
- Tests coverage is still low as mentioned before, but coverage and tests are available. Added v0.1 of [Test Documentation](docs/week2.md) which only includes test coverage for now.
- This week was mainly spent on implementing UI still and learning about A*. Cell_size with current UI feels too small. Tried to experiment with resolution sizes but scaling cell_size to 4 would require scaling resolution quite high already. Will consider changes after implementing visualization of the pathfinding algorithm paths, cause I think what really matters is how it looks when traversing the path. 

Hours spent: 8h
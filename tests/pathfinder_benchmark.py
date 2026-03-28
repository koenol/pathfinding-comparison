"""
Tool for benchmarking pathfinder algorithm.
    -n, --flag (int): how many times the test is run
    -r, --report (str): report individual comparison, options [on/off]
"""
import argparse
import random
from src.astar import Astar
from src.jps import Jps
from src.map_generator import MapGenerator

BLOCKED_TILES = {"@", "O", "T"}

def main():
    parser = argparse.ArgumentParser(description="Pathfinder Benchmark")
    parser.add_argument("-n", "--flag", type=int, default=1)
    parser.add_argument("-r", "--report", choices=["on", "off"], default="on")
    args = parser.parse_args()
    n = args.flag
    report = args.report

    run_benchmark(n, report)

def get_random_xy(grid):
	"""Pick a random passable point"""
	rows = len(grid)
	cols = len(grid[0])
	while True:
		x = random.randint(0, cols - 1)
		y = random.randint(0, rows - 1)
		if grid[y][x] not in BLOCKED_TILES:
			return (x, y)

def update_comparison(astar_value, jps_value, counts):
    """Update A* vs JPS pathfinders comparison"""
    if astar_value < jps_value:
        counts["astar"] += 1
    elif jps_value < astar_value:
        counts["jps"] += 1
    else:
        counts["equal"] += 1

def run_benchmark(n, report):
    map_generator = MapGenerator()
    astar = Astar()
    jps = Jps()
    map_names = map_generator.list_maps()
    runtime_counts = {"astar": 0, "jps": 0, "equal": 0}
    expanded_counts = {"astar": 0, "jps": 0, "equal": 0}
    path_length_counts = {"astar": 0, "jps": 0, "equal": 0}

    for _ in range(n):
        map_name = random.choice(map_names)
        game_map = map_generator.load_map_by_name(map_name)

        start = get_random_xy(game_map)
        goal = get_random_xy(game_map)
        while goal == start:
            goal = get_random_xy(game_map)

        astar_path = astar.find_path(game_map, start, goal)
        jps_path = jps.find_path(game_map, start, goal)

        astar_runtime = astar.stats["elapsed_ms"]
        jps_runtime = jps.stats["elapsed_ms"]
        astar_expanded = astar.stats["expanded_nodes"]
        jps_expanded = jps.stats["expanded_nodes"]
        astar_path_len = len(astar_path)
        jps_path_len = len(jps_path)

        update_comparison(astar_runtime, jps_runtime, runtime_counts)
        update_comparison(astar_expanded, jps_expanded, expanded_counts)
        update_comparison(astar_path_len, jps_path_len, path_length_counts)

        if report == "on":
            print(
                f"{map_name}: "
                f"A* "
                f"runtime={astar_runtime:.3f}ms, "
                f"expanded_nodes={astar_expanded}, "
                f"path_length={astar_path_len} | "
                f"JPS "
                f"runtime={jps_runtime:.3f}ms, "
                f"expanded_nodes={jps_expanded}, "
                f"path_length={jps_path_len}"
            )

    print("\nSummary:")
    print(
        "Runtime faster: "
        f"A*: {runtime_counts['astar']}, "
        f"JPS: {runtime_counts['jps']}, "
        f"Equal: {runtime_counts['equal']}"
    )
    print(
        "Expanded fewer nodes: "
        f"A*: {expanded_counts['astar']}, "
        f"JPS: {expanded_counts['jps']}, "
        f"Equal: {expanded_counts['equal']}"
    )
    print(
        "Shorter path length: "
        f"A*: {path_length_counts['astar']}, "
        f"JPS: {path_length_counts['jps']}, "
        f"Equal: {path_length_counts['equal']}"
    )

if __name__ == '__main__':
    main()
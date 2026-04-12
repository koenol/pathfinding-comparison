"""Pathfinder base class for A* and JPS"""
import math
from time import perf_counter

class Pathfinder:
	"""Pathfinder base class"""
	BLOCKED_TILES = {"@", "O", "T"}
	DIRECTIONS = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1),
		(1, 1),
		(1, -1),
		(-1, 1),
		(-1, -1),
	]

	def __init__(self):
		"""Init shared pathfinder state"""
		self.stats = {
			"elapsed_ms": 0.0,
		}
		self.expanded_nodes = []
		self.scanned_nodes = []
		self.expanded_nodes_set = set()
		self.scanned_nodes_set = set()

	def h(self, point1, point2):
		"""Calculate octile distance"""
		x1, y1 = point1
		x2, y2 = point2
		dx = abs(x1 - x2)
		dy = abs(y1 - y2)
		return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)

	def is_in_bounds(self, grid, point):
		"""Check bounds"""
		x, y = point
		rows = len(grid)
		cols = len(grid[0])
		return 0 <= x < cols and 0 <= y < rows

	def is_passable(self, grid, point):
		"""Check whether tile is passable"""
		x, y = point
		return grid[y][x] not in self.BLOCKED_TILES

	def update_stats(self, elapsed_ms):
		"""Store stats"""
		self.stats = {
			"elapsed_ms": elapsed_ms,
		}

	def add_expanded_node(self, point):
		"""Store expanded nodes"""
		if point not in self.expanded_nodes_set:
			self.expanded_nodes_set.add(point)
			self.expanded_nodes.append(point)

	def add_scanned_node(self, point):
		"""Store scanned nodes"""
		if point not in self.scanned_nodes_set:
			self.scanned_nodes_set.add(point)
			self.scanned_nodes.append(point)

	def reset_search_state(self):
		"""Reset search"""
		self.expanded_nodes = []
		self.scanned_nodes = []
		self.expanded_nodes_set = set()
		self.scanned_nodes_set = set()

	def get_path_search_status(self, grid, start, goal):
		"""Valdidate search start"""
		if not start or not goal:
			self.update_stats(0.0)
			return []
		if not self.is_in_bounds(grid, start) or not self.is_in_bounds(grid, goal):
			self.update_stats(0.0)
			return []
		if not self.is_passable(grid, start) or not self.is_passable(grid, goal):
			self.update_stats(0.0)
			return []
		if start == goal:
			self.add_expanded_node(start)
			self.add_scanned_node(start)
			self.update_stats(0.0)
			return [start]
		return None

	def new_search(self, grid, start, goal):
		"""Start new search"""
		self.reset_search_state()
		early_result = self.get_path_search_status(grid, start, goal)
		if early_result is not None:
			return early_result, None
		return None, perf_counter()

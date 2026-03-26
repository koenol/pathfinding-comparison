"""Jump Point Search (JPS) Algorithm"""
from queue import PriorityQueue

class Jps:
	"""JPS pathfinder"""
	BLOCKED_TILES = {"@", "O", "T"}
	def __init__(self):
		"""Init. JPS"""
		self.running = False

	def start_pathfinder(self):
		"""Set pathfinder status to True"""
		self.running = True

	def stop_pathfinder(self):
		"""Set pathfinder status to False"""
		self.running = False

	def h(self, point1, point2):
		"""Calculate Manhattan distance"""
		x1, y1 = point1
		x2, y2 = point2
		return abs(x1 - x2) + abs(y1 - y2)

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

	def directions(self):
		"""Return directions"""
		return [
			(1, 0),
			(-1, 0),
			(0, 1),
			(0, -1),
		]

	def get_neighbors(self, grid, point):
		"""Return valid neighbors"""
		x, y = point
		neighbors = []
		for dx, dy in self.directions():
			next_point = (x + dx, y + dy)
			if self.is_in_bounds(grid, next_point) and self.is_passable(grid, next_point):
				neighbors.append(next_point)
		return neighbors

	def convert_value(self, value):
		"""Convert value to sign value: -1, 0, or 1"""
		if value == 0:
			return 0
		if value > 0:
			return 1
		return -1

	def move_cost(self, point1, point2):
		"""Return movement cost """
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


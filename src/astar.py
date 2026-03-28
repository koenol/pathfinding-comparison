"""A* Algorithm:
f(n) = g(n) + h(n)
g(n) = cost of path from the start node to n
h(n) = heuristic calc from n to goal
"""
import math
import heapq
from time import perf_counter

class Astar:
	"""A* pathfinder"""
	BLOCKED_TILES = {"@", "O", "T"}
	DIRECTIONS = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1),
	]
	def __init__(self):
		"""Init. A*"""
		self.running = False
		self.stats = {
			"expanded_nodes": 0,
			"elapsed_ms": 0.0,
		}

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

	def get_neighbors(self, grid, point):
		"""Return valid neighbor tiles"""
		x, y = point
		neighbors = []

		for dx, dy in self.DIRECTIONS:
			next_point = (x + dx, y + dy)
			if self.is_in_bounds(grid, next_point) and self.is_passable(grid, next_point):
				neighbors.append(next_point)
		return neighbors

	def move_cost(self, point1, point2):
		"""Return movement cost"""
		dx = abs(point1[0] - point2[0])
		dy = abs(point1[1] - point2[1])
		return math.sqrt(2) if dx == 1 and dy == 1 else 1

	def find_path(self, grid, start, goal):
		"""Start A* pathfinder"""
		if not start or not goal:
			self.update_stats(0, 0.0)
			return []
		if not self.is_in_bounds(grid, start) or not self.is_in_bounds(grid, goal):
			self.update_stats(0, 0.0)
			return []
		if not self.is_passable(grid, start) or not self.is_passable(grid, goal):
			self.update_stats(0, 0.0)
			return []
		if start == goal:
			self.update_stats(1, 0.0)
			return [start]

		started = perf_counter()
		deck = []
		heapq.heappush(deck, (0, start))
		expanded = 0

		origin = {start: None}
		g_score = {start: 0}

		while deck:
			_, current = heapq.heappop(deck)
			expanded += 1

			if current == goal:
				path = []
				while current is not None:
					path.append(current)
					current = origin[current]
				path.reverse()
				elapsed_ms = (perf_counter() - started) * 1000
				self.update_stats(expanded, elapsed_ms)
				return path

			for neighbor in self.get_neighbors(grid, current):
				tentative_g_score = g_score[current] + self.move_cost(current, neighbor)
				if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
					origin[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score = tentative_g_score + self.h(neighbor, goal)
					heapq.heappush(deck, (f_score, neighbor))

		elapsed_ms = (perf_counter() - started) * 1000
		self.update_stats(expanded, elapsed_ms)
		return []

	def update_stats(self, expanded_nodes, elapsed_ms):
		"""Store stats"""
		self.stats = {
			"expanded_nodes": expanded_nodes,
			"elapsed_ms": elapsed_ms,
		}

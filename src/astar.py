"""A* Algorithm:
f(n) = g(n) + h(n)
g(n) = cost of path from the start node to n
h(n) = heuristic calc from n to goal
"""
import math
import heapq
from time import perf_counter

try:
	from pathfinder import Pathfinder
except ImportError:
	from .pathfinder import Pathfinder

class Astar(Pathfinder):
	"""A* pathfinder"""
	def __init__(self):
		"""Init. A*"""
		super().__init__()

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
		issue, started = self.new_search(grid, start, goal)
		if issue is not None:
			return issue

		deck = []
		heapq.heappush(deck, (0, start))
		expanded = 0

		origin = {start: None}
		g_score = {start: 0}

		while deck:
			_, current = heapq.heappop(deck)
			expanded += 1
			self.add_expanded_node(current)

			if current == goal:
				path = []
				while current is not None:
					path.append(current)
					current = origin[current]
				path.reverse()
				elapsed_ms = (perf_counter() - started) * 1000
				self.update_stats(elapsed_ms)
				return path

			for neighbor in self.get_neighbors(grid, current):
				self.add_scanned_node(neighbor)
				tentative_g_score = g_score[current] + self.move_cost(current, neighbor)
				if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
					origin[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score = tentative_g_score + self.h(neighbor, goal)
					heapq.heappush(deck, (f_score, neighbor))

		elapsed_ms = (perf_counter() - started) * 1000
		self.update_stats(elapsed_ms)
		return []

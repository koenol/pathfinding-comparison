"""Jump Point Search (JPS) Algorithm"""

import math
import heapq
from time import perf_counter

try:
	from .pathfinder import Pathfinder
except ImportError:
	from pathfinder import Pathfinder


class Jps(Pathfinder):
	"""JPS pathfinder"""

	def is_walkable(self, grid, point):
		"""Check both map bounds and passability"""
		return self.is_in_bounds(grid, point) and self.is_passable(grid, point)

	def get_neighbors(self, grid, point, parent):
		"""Return valid neighbors"""
		x, y = point
		if parent is None:
			neighbors_deck = []
			for dx, dy in self.DIRECTIONS:
				next_point = (x + dx, y + dy)
				if self.is_walkable(grid, next_point):
					neighbors_deck.append(next_point)
			return neighbors_deck
		dx, dy = self.get_normalized_direction(parent, point)
		neighbors_deck = []

		if dx != 0 and dy != 0:
			for next_point in ((x + dx, y), (x, y + dy), (x + dx, y + dy)):
				if self.is_walkable(grid, next_point):
					neighbors_deck.append(next_point)

			if (not self.is_walkable(grid, (x - dx, y)) and
				self.is_walkable(grid, (x - dx, y + dy))):
				neighbors_deck.append((x - dx, y + dy))
			if (not self.is_walkable(grid, (x, y - dy)) and
				self.is_walkable(grid, (x + dx, y - dy))):
				neighbors_deck.append((x + dx, y - dy))
		elif dx != 0:
			next_point = (x + dx, y)
			if self.is_walkable(grid, next_point):
				neighbors_deck.append(next_point)

			if (not self.is_walkable(grid, (x, y + 1)) and
				self.is_walkable(grid, (x + dx, y + 1))):
				neighbors_deck.append((x + dx, y + 1))
			if (not self.is_walkable(grid, (x, y - 1)) and
				self.is_walkable(grid, (x + dx, y - 1))):
				neighbors_deck.append((x + dx, y - 1))
		else:
			next_point = (x, y + dy)
			if self.is_walkable(grid, next_point):
				neighbors_deck.append(next_point)

			if (not self.is_walkable(grid, (x + 1, y)) and
				self.is_walkable(grid, (x + 1, y + dy))):
				neighbors_deck.append((x + 1, y + dy))
			if (not self.is_walkable(grid, (x - 1, y)) and
				self.is_walkable(grid, (x - 1, y + dy))):
				neighbors_deck.append((x - 1, y + dy))
		return neighbors_deck

	def move_cost(self, point1, point2):
		"""Return move cost for all segments"""
		dx = abs(point2[0] - point1[0])
		dy = abs(point2[1] - point1[1])
		diagonal_segment = min(dx, dy)
		straight_segment = max(dx, dy) - diagonal_segment
		return diagonal_segment * math.sqrt(2) + straight_segment

	def get_normalized_direction(self, point1, point2):
		"""normalized movement direction"""
		dx = point2[0] - point1[0]
		dy = point2[1] - point1[1]
		return (
			0 if dx == 0 else (1 if dx > 0 else -1),
			0 if dy == 0 else (1 if dy > 0 else -1),
		)

	def check_forced_neighbor(self, grid, point, direction):
		"""Check if the node has any forced neighbors"""
		x, y = point
		dx, dy = direction

		if dx != 0 and dy != 0:
			if (not self.is_walkable(grid, (x - dx, y)) and
				self.is_walkable(grid, (x - dx, y + dy))):
				return True
			if (not self.is_walkable(grid, (x, y - dy)) and
				self.is_walkable(grid, (x + dx, y - dy))):
				return True
			return False

		if dx != 0:
			if (not self.is_walkable(grid, (x, y + 1)) and
				self.is_walkable(grid, (x + dx, y + 1))):
				return True
			if (not self.is_walkable(grid, (x, y - 1)) and
				self.is_walkable(grid, (x + dx, y - 1))):
				return True
			return False

		if (not self.is_walkable(grid, (x + 1, y)) and
			self.is_walkable(grid, (x + 1, y + dy))):
			return True
		if (not self.is_walkable(grid, (x - 1, y)) and
			self.is_walkable(grid, (x - 1, y + dy))):
			return True
		return False

	def jps_jump(self, grid, point, direction, goal):
		"""Jump in set direction"""
		dx, dy = direction
		next_point = (point[0] + dx, point[1] + dy)

		if not self.is_walkable(grid, next_point):
			return None
		self.add_scanned_node(next_point)
		if next_point == goal:
			return next_point
		if self.check_forced_neighbor(grid, next_point, direction):
			return next_point
		if dx != 0 and dy != 0:
			if self.jps_jump(grid, next_point, (dx, 0), goal) is not None:
				return next_point
			if self.jps_jump(grid, next_point, (0, dy), goal) is not None:
				return next_point
		return self.jps_jump(grid, next_point, direction, goal)

	def expand_path(self, point1, point2):
		"""JPS segments to steps"""
		dx, dy = self.get_normalized_direction(point1, point2)
		current = point1
		segment_list = [point1]

		while current != point2:
			current = (current[0] + dx, current[1] + dy)
			segment_list.append(current)
		return segment_list

	def reconstruct_path(self, parents, goal):
		"""Reconstruct JPS path"""
		jps_deck = []
		current = goal
		while current is not None:
			jps_deck.append(current)
			current = parents[current]
		jps_deck.reverse()

		path = [jps_deck[0]]
		for index in range(1, len(jps_deck)):
			segment = self.expand_path(jps_deck[index - 1], jps_deck[index])
			path.extend(segment[1:])
		return path

	def find_path(self, grid, start, goal):
		"""Start JPS pathfinder"""
		issue, started = self.new_search(grid, start, goal)
		if issue is not None:
			return issue

		open_deck = []
		heapq.heappush(open_deck, (0.0, start))
		expanded = 0

		parents = {start: None}
		g_score = {start: 0.0}

		while open_deck:
			_, current = heapq.heappop(open_deck)
			expanded += 1
			self.add_expanded_node(current)

			if current == goal:
				path = self.reconstruct_path(parents, goal)
				elapsed_ms = (perf_counter() - started) * 1000
				self.update_stats(elapsed_ms)
				return path

			current_parent = parents[current]
			for neighbor in self.get_neighbors(grid, current, current_parent):
				self.add_scanned_node(neighbor)
				direction = self.get_normalized_direction(current, neighbor)
				jump_point = self.jps_jump(grid, current, direction, goal)

				if jump_point is None:
					continue

				tentative_g_score = g_score[current] + self.move_cost(current, jump_point)
				if (jump_point not in g_score or
					tentative_g_score < g_score[jump_point]):
					parents[jump_point] = current
					g_score[jump_point] = tentative_g_score
					f_score = tentative_g_score + self.h(jump_point, goal)
					heapq.heappush(open_deck, (f_score, jump_point))

		elapsed_ms = (perf_counter() - started) * 1000
		self.update_stats(elapsed_ms)
		return []

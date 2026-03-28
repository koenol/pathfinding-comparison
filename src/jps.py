"""Jump Point Search (JPS) Algorithm"""
import heapq
from time import perf_counter

class Jps:
	"""JPS pathfinder"""
	BLOCKED_TILES = {"@", "O", "T"}
	DIRECTIONS = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1),
	]

	def __init__(self):
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
		"""Return valid neighbors"""
		x, y = point
		neighbors = []
		for dx, dy in self.DIRECTIONS:
			next_point = (x + dx, y + dy)
			if self.can_walk(grid, next_point):
				neighbors.append(next_point)
		return neighbors

	def move_cost(self, point1, point2):
		"""Return movement cost """
		return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
	
	def can_walk(self, grid, point):
		"""Check node is within bounds and passable"""
		return self.is_in_bounds(grid, point) and self.is_passable(grid, point)

	def check_forced_neighbor(self, grid, point, direction):
		"""Check if the node has any forced neighbors"""
		x, y = point
		dx, dy = direction

		if dx != 0:
			up = (x, y - 1)
			down = (x, y + 1)
			prev_up = (x - dx, y - 1)
			prev_down = (x - dx, y + 1)
			if self.can_walk(grid, up) and not self.can_walk(grid, prev_up):
				return True
			if self.can_walk(grid, down) and not self.can_walk(grid, prev_down):
				return True
		if dy != 0:
			left = (x - 1, y)
			right = (x + 1, y)
			prev_left = (x - 1, y - dy)
			prev_right = (x + 1, y - dy)
			if self.can_walk(grid, left) and not self.can_walk(grid, prev_left):
				return True
			if self.can_walk(grid, right) and not self.can_walk(grid, prev_right):
				return True
		return False

	def directions(self, previous, current):
		dx = current[0] - previous[0]
		dy = current[1] - previous[1]
		if dx != 0:
			dx = 1 if dx > 0 else -1
		if dy != 0:
			dy = 1 if dy > 0 else -1
		return dx, dy

	def append_dir(self, directions, direction):
		"""Append direction"""
		if direction not in directions:
			directions.append(direction)

	def prune_directions(self, grid, current, previous, goal):
		"""Prune neighbors based on current travel direction."""
		if previous is None:
			return self.DIRECTIONS

		x, y = current
		dx, dy = self.directions(previous, current)
		dirs_deck = []

		forward = (dx, dy)
		forward_point = (x + dx, y + dy)
		forward_walkable = self.can_walk(grid, forward_point)
		if forward_walkable:
			self.append_dir(dirs_deck, forward)

		if dx != 0:
			if not forward_walkable or x == goal[0]:
				if self.can_walk(grid, (x, y - 1)):
					self.append_dir(dirs_deck, (0, -1))
				if self.can_walk(grid, (x, y + 1)):
					self.append_dir(dirs_deck, (0, 1))

			up = (x, y - 1)
			down = (x, y + 1)
			prev_up = (x - dx, y - 1)
			prev_down = (x - dx, y + 1)
			if self.can_walk(grid, up) and not self.can_walk(grid, prev_up):
				self.append_dir(dirs_deck, (0, -1))
			if self.can_walk(grid, down) and not self.can_walk(grid, prev_down):
				self.append_dir(dirs_deck, (0, 1))

		if dy != 0:
			if not forward_walkable or y == goal[1]:
				if self.can_walk(grid, (x - 1, y)):
					self.append_dir(dirs_deck, (-1, 0))
				if self.can_walk(grid, (x + 1, y)):
					self.append_dir(dirs_deck, (1, 0))

			left = (x - 1, y)
			right = (x + 1, y)
			prev_left = (x - 1, y - dy)
			prev_right = (x + 1, y - dy)
			if self.can_walk(grid, left) and not self.can_walk(grid, prev_left):
				self.append_dir(dirs_deck, (-1, 0))
			if self.can_walk(grid, right) and not self.can_walk(grid, prev_right):
				self.append_dir(dirs_deck, (1, 0))
		return dirs_deck

	def jps_jump(self, grid, start, direction, goal):
		"""Jump in set direction"""
		dx, dy = direction
		x, y = start

		while True:
			x += dx
			y += dy
			point = (x, y)

			if not self.can_walk(grid, point):
				return None
			if point == goal:
				return point

			next_point = (x + dx, y + dy)
			if not self.can_walk(grid, next_point):
				return point
			if self.check_forced_neighbor(grid, point, direction):
				return point
			if (dx != 0 and x == goal[0]) or (dy != 0 and y == goal[1]):
				return point

	def check_successors(self, grid, current, previous, goal):
		"""Check possible successors for current node"""
		successors = []
		for direction in self.prune_directions(grid, current, previous, goal):
			jump_point = self.jps_jump(grid, current, direction, goal)
			if jump_point is not None:
				successors.append(jump_point)
		return successors

	def expand_path(self, origin, destination):
		"""Check all intermediate points on the line"""
		x1, y1 = origin
		x2, y2 = destination
		dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
		dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)
		points = []
		x, y = x1, y1
		while (x, y) != (x2, y2):
			x += dx
			y += dy
			points.append((x, y))
		return points

	def reconstruct_path(self, origin, start, goal):
		"""Reconstruct JPS path"""
		jps_deck = []
		current = goal
		while current is not None:
			jps_deck.append(current)
			current = origin[current]
		jps_deck.reverse()

		if not jps_deck:
			return []

		full_path = [jps_deck[0]]
		for i in range(1, len(jps_deck)):
			full_path.extend(self.expand_path(jps_deck[i - 1], jps_deck[i]))
		if full_path[0] != start:
			full_path.insert(0, start)
		return full_path

	def find_path(self, grid, start, goal):
		"""Start JPS pathfinder"""
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
		open_deck = []
		heapq.heappush(open_deck, (self.h(start, goal), start))

		came_from = {start: None}
		g_score = {start: 0}
		expanded = 0

		while open_deck:
			_, current = heapq.heappop(open_deck)
			expanded += 1

			if current == goal:
				elapsed_ms = (perf_counter() - started) * 1000
				self.update_stats(expanded, elapsed_ms)
				return self.reconstruct_path(came_from, start, goal)

			previous = came_from[current]
			for neighbor in self.check_successors(grid, current, previous, goal):
				tentative_g_score = g_score[current] + self.move_cost(current, neighbor)
				if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
					came_from[neighbor] = current
					g_score[neighbor] = tentative_g_score
					f_score = tentative_g_score + self.h(neighbor, goal)
					heapq.heappush(open_deck, (f_score, neighbor))

		elapsed_ms = (perf_counter() - started) * 1000
		self.update_stats(expanded, elapsed_ms)
		return []

	def update_stats(self, expanded_nodes, elapsed_ms):
		"""Store stats."""
		self.stats = {
			"expanded_nodes": expanded_nodes,
			"elapsed_ms": elapsed_ms,
		}

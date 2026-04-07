"""Map handler"""

import pygame

class MapHandler:
	"""Map handler class"""
	def __init__(self):
		"""Init. MapHandler"""
		self.start_position = None
		self.goal_position = None
		self.start_color = (0, 255, 0)
		self.goal_color = (125, 0, 125)
		self.scanned_color = (80, 170, 255)
		self.expanded_color = (255, 255, 0)
		self.scanned_nodes = []
		self.expanded_nodes = []
		self.path = []
		self.path_color = (255, 80, 80)

	def update_selected_position(self, x: int, y: int):
		"""Set start first & goal"""
		if self.start_position is None:
			self.start_position = (x, y)
		elif self.goal_position is None:
			self.goal_position = (x, y)

	def draw_selected_tiles(
		self,
		screen: pygame.Surface,
		offset_x: int = 10,
		offset_y: int = 50,
		cell_size: int = 1,
	):
		"""Draw colored tiles"""
		for x, y in self.scanned_nodes:
			rect = pygame.Rect(
				offset_x + x * cell_size,
				offset_y + y * cell_size,
				cell_size,
				cell_size,
			)
			pygame.draw.rect(screen, self.scanned_color, rect)

		for x, y in self.expanded_nodes:
			rect = pygame.Rect(
				offset_x + x * cell_size,
				offset_y + y * cell_size,
				cell_size,
				cell_size,
			)
			pygame.draw.rect(screen, self.expanded_color, rect)

		for x, y in self.path:
			rect = pygame.Rect(
				offset_x + x * cell_size,
				offset_y + y * cell_size,
				cell_size,
				cell_size,
			)
			pygame.draw.rect(screen, self.path_color, rect)

		if len(self.path) >= 2:
			line_points = [
				(
					offset_x + x * cell_size + cell_size // 2,
					offset_y + y * cell_size + cell_size // 2,
				)
				for x, y in self.path
			]
			pygame.draw.lines(screen, self.path_color, False, line_points, max(1, cell_size))

		if self.start_position is not None:
			x, y = self.start_position
			rect = pygame.Rect(
				offset_x + x * cell_size,
				offset_y + y * cell_size,
				cell_size,
				cell_size,
			)
			pygame.draw.rect(screen, self.start_color, rect)

		if self.goal_position is not None:
			x, y = self.goal_position
			rect = pygame.Rect(
				offset_x + x * cell_size,
				offset_y + y * cell_size,
				cell_size,
				cell_size,
			)
			pygame.draw.rect(screen, self.goal_color, rect)

	def reset_positions(self):
		"""Reset positions"""
		self.start_position = None
		self.goal_position = None
		self.scanned_nodes = []
		self.expanded_nodes = []
		self.path = []

	def set_path(self, path):
		"""Store path"""
		self.path = path

	def get_start_position(self):
		"""Get start coordinates"""
		return self.start_position

	def get_goal_position(self):
		"""Get goal coordinates"""
		return self.goal_position

	def set_expanded_nodes(self, expanded_nodes):
		"""Store expanded nodes"""
		self.expanded_nodes = list(dict.fromkeys(expanded_nodes))

	def set_scanned_nodes(self, scanned_nodes):
		"""Store scanned nodes"""
		self.scanned_nodes = list(dict.fromkeys(scanned_nodes))
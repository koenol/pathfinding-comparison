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

	def reset_positions(self) -> None:
		"""Reset positions"""
		self.start_position = None
		self.goal_position = None

	def get_start_position(self):
		"""Get start coordinates"""
		return self.start_position

	def get_goal_position(self):
		"""Get goal coordinates"""
		return self.goal_position

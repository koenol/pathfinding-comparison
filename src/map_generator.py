"""Map generation and rendering utilities."""

import pygame

class MapGenerator:
	def __init__(self, grid_size: int = 10, cell_size: int = 10):
		self.grid_size = grid_size
		self.cell_size = cell_size

	def generate_map(self) -> list[list[int]]:
		"""Generate a grid using the configured grid size."""
		grid = []
		for _ in range(self.grid_size):
			row = []
			for _ in range(self.grid_size):
				tile = 1
				row.append(tile)
			grid.append(row)
		return grid

	def draw_map(self, screen: pygame.Surface, grid: list[list[int]]):
		"""Draw the generated map to the screen."""
		for y, row in enumerate(grid):
			for x, tile in enumerate(row):
				color = (220, 220, 220)
				rect = pygame.Rect(
					x * self.cell_size,
					y * self.cell_size,
					self.cell_size,
					self.cell_size,
				)
				pygame.draw.rect(screen, color, rect)
				pygame.draw.rect(screen, (100, 100, 100), rect, 1)

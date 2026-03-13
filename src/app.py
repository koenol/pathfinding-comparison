"""Simple 2D map generator"""

import pygame

GRID_SIZE = 10
CELL_SIZE = 20

def generate_map(size: int) -> list[list[int]]:
	"""Generate a size x size 2D grid map."""
	grid = []
	for _ in range(size):
		row = []
		for _ in range(size):
			tile = 1
			row.append(tile)
		grid.append(row)
	return grid

def draw_map(screen: pygame.Surface, grid: list[list[int]], cell_size: int):
	"""Draw the generated map to the screen."""
	for y, row in enumerate(grid):
		for x, tile in enumerate(row):
			color = (220, 220, 220)
			rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
			pygame.draw.rect(screen, color, rect)
			pygame.draw.rect(screen, (100, 100, 100), rect, 1)

def main():
	pygame.init()
	window_size = GRID_SIZE * CELL_SIZE
	screen = pygame.display.set_mode((window_size, window_size))
	pygame.display.set_caption("Pathfinding Algorithm Comparison")
	grid = generate_map(GRID_SIZE)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		draw_map(screen, grid, CELL_SIZE)
		pygame.display.flip()

	pygame.quit()


if __name__ == "__main__":
	main()

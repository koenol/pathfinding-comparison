"""Simple 2D map generator"""

import pygame
from .map_generator import MapGenerator
from .ui import UI

def main():
	"""Main loop"""
	pygame.init()
	screen = pygame.display.set_mode((1024, 768))
	pygame.display.set_caption("Pathfinding Algorithm Comparison")
	map_generator = MapGenerator()
	map_names = map_generator.list_maps()
	ui = UI(map_names)
	grid = map_generator.load_first_map()
	ui.set_grid_dimensions(len(grid[0]), len(grid))

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			result = ui.handle_event(event)
			if result and result in map_names:
				grid = map_generator.load_map_by_name(result)
				ui.set_grid_dimensions(len(grid[0]), len(grid))

		ui.set_grid_dimensions(len(grid[0]), len(grid))
		screen.fill((25, 25, 30))
		ui.draw_selector(screen)
		map_generator.generate_map(screen, grid)
		ui.map_handler.draw_selected_tiles(
			screen,
			offset_x=ui.map_offset_x,
			offset_y=ui.map_offset_y,
			cell_size=ui.cell_size,
		)
		ui.draw_dropdown_list(screen)
		ui.draw_xy(screen)
		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()
